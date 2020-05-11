from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdefgh"

codes = [
    {
        'method_name' : 'trial 1',
        'method_code' : 'code here!'
    }, 
    {
        'method_name' : 'trial 2',
        'method_code' : 'print("hello there!")'
    }
]

@app.route('/')
def index():
    return render_template("index.html")

def update_codes(query):
    # Note For Akhil Chandra
    # This is where you update the rank list : codes 
    # after the search is done, query is the search string. 
    global codes
    codes = []
    url = "http://localhost:9200/_search?pretty"
    query_string = str(query) #in case the query isnt a string, who knows :)
    #use the 'headers' parameter to set the HTTP headers:
    data = '''{"query": { "simple_query_string" : {"fields" : ["full_doc"],"query" : "''' + query_string + '"}}}'
    x = requests.post(url, headers = {"Content-Type": "application/json"}, data = data)
    #print(x.text)
    print(x.json()) #it is a json object!, and it prints onto the 
    x_dict = x.json() #it reads it as a dictionary!
    rank = 1
    #instance of elem as given below:
    #{'_index': 'valid', '_type': 
    # '_doc', '_id': '11407', 
    # '_score': 13.56068, 
    # '_source': {'repo': 'trimou/trimou', 'path': 'core/src/main/java/org/trimou/engine/context/DefaultExecutionContext.java', 'func_name': 'DefaultExecutionContext.resolveLeadingContextObject', 'original_string': 'private Object resolveLeadingContextObject(String name, ValueWrapper value,\n            AtomicReference<Hint> hintRef) {\n\n        Object leading = resolveContextObject(name, value, hintRef);\n\n        if (leading == null) {\n            // Leading context object not found - try to resolve context\n            // unrelated objects (JNDI lookup, CDI, etc.)\n            Hint hint = hintRef != null ? hintRef.get() : null;\n            if (hint != null) {\n                leading = hint.resolve(null, name, value);\n            }\n            if (leading == null) {\n                leading = resolve(null, name, value, hint == null\n                        && hintRef != null);\n            }\n        }\n        return leading;\n    }', 'language': 'java', 'code': 'private Object resolveLeadingContextObject(String name, ValueWrapper value,\n            AtomicReference<Hint> hintRef) {\n\n        Object leading = resolveContextObject(name, value, hintRef);\n\n        if (leading == null) {\n            // Leading context object not found - try to resolve context\n            // unrelated objects (JNDI lookup, CDI, etc.)\n            Hint hint = hintRef != null ? hintRef.get() : null;\n            if (hint != null) {\n                leading = hint.resolve(null, name, value);\n            }\n            if (leading == null) {\n                leading = resolve(null, name, value, hint == null\n                        && hintRef != null);\n            }\n        }\n        return leading;\n    }', 'code_tokens': ['private', 'Object', 'resolveLeadingContextObject', '(', 'String', 'name', ',', 'ValueWrapper', 'value', ',', 'AtomicReference', '<', 'Hint', '>', 'hintRef', ')', '{', 'Object', 'leading', '=', 'resolveContextObject', '(', 'name', ',', 'value', ',', 'hintRef', ')', ';', 'if', '(', 'leading', '==', 'null', ')', '{', '// Leading context object not found - try to resolve context', '// unrelated objects (JNDI lookup, CDI, etc.)', 'Hint', 'hint', '=', 'hintRef', '!=', 'null', '?', 'hintRef', '.', 'get', '(', ')', ':', 'null', ';', 'if', '(', 'hint', '!=', 'null', ')', '{', 'leading', '=', 'hint', '.', 'resolve', '(', 'null', ',', 'name', ',', 'value', ')', ';', '}', 'if', '(', 'leading', '==', 'null', ')', '{', 'leading', '=', 'resolve', '(', 'null', ',', 'name', ',', 'value', ',', 'hint', '==', 'null', '&&', 'hintRef', '!=', 'null', ')', ';', '}', '}', 'return', 'leading', ';', '}'], 'docstring': 'Resolve the leading context object (the first part of the key). E.g.\n<code>foo</code> in <code>{{foo.bar.name}}</code> may identify a property\nof some context object on the stack (passed data, section iteration,\nnested context, ...), or some context and data unrelated object (e.g. CDI\nbean).\n\n@param name\n@param value\nThe value wrapper - ResolutionContext\n@param hintRef\n@return the resolved leading context object\n@see Hint', 'docstring_tokens': ['Resolve', 'the', 'leading', 'context', 'object', '(', 'the', 'first', 'part', 'of', 'the', 'key', ')', '.', 'E', '.', 'g', '.', '<code', '>', 'foo<', '/', 'code', '>', 'in', '<code', '>', '{{', 'foo', '.', 'bar', '.', 'name', '}}', '<', '/', 'code', '>', 'may', 'identify', 'a', 'property', 'of', 'some', 'context', 'object', 'on', 'the', 'stack', '(', 'passed', 'data', 'section', 'iteration', 'nested', 'context', '...', ')', 'or', 'some', 'context', 'and', 'data', 'unrelated', 'object', '(', 'e', '.', 'g', '.', 'CDI', 'bean', ')', '.'], 'sha': 'ae45d77d4bd8b2c71b41006908b8a0a784ad9058', 'url': 'https://github.com/trimou/trimou/blob/ae45d77d4bd8b2c71b41006908b8a0a784ad9058/core/src/main/java/org/trimou/engine/context/DefaultExecutionContext.java#L236-L254', 'partition': 'valid', 'func_name_prediction': 'resolve', 'full_doc': 'resolve resolve leading context object Resolve the leading context object ( the first part of the key ) . E . g . <code > foo< / code > in <code > {{ foo . bar . name }} < / code > may identify a property of some context object on the stack ( passed data section iteration nested context ... ) or some context and data unrelated object ( e . g . CDI bean ) .  private Object resolveLeadingContextObject ( String name , ValueWrapper value , AtomicReference < Hint > hintRef ) { Object leading = resolveContextObject ( name , value , hintRef ) ; if ( leading == null ) { // Leading context object not found - try to resolve context // unrelated objects (JNDI lookup, CDI, etc.) Hint hint = hintRef != null ? hintRef . get ( ) : null ; if ( hint != null ) { leading = hint . resolve ( null , name , value ) ; } if ( leading == null ) { leading = resolve ( null , name , value , hint == null && hintRef != null ) ; } } return leading ; } '}}
    if len(x_dict["hits"]["hits"]) == 0:
	    codes.append({
	        'method_name':str(query)+str(rank),
	        'method_code':"There are no hits!"
	    })
    else:
	    for elem in x_dict["hits"]["hits"]:
	        output = "relavence_score: \n \t" + str(elem['_score']) + '\n'
	        output = output + "document_id: \n \t" + str(elem['_index']) + str(elem['_type']) + str(elem['_id']) + '\n'
	        output = output + "code: \n \t" + str(elem['_source']["original_string"]) + '\n'
	        codes.append({
	            'method_name':str(query)+' '+str(rank),
	            'method_code':output
	        })
	        rank = rank	+ 1
    return codes

@app.route('/demo', methods=['GET','POST'])
def demo():
    global codes
    if request.method == "POST":
        query = request.form["query"]
        codes = update_codes(query)
    else:
        codes = []
    return render_template("demo.html", title = "demo", code = codes, len = len(codes))

if __name__=="__main__":
    app.run(debug=True)