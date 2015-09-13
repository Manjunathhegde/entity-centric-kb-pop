import web
import json, logging, html_helper
from getEntityInfo import Main
from fileReader import getList

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        query = web.ctx.get('query')
        html = html_helper.HTMLHelper()
        if query:
            arr = query.split('=')
            if len(arr)>1:
                filename = arr[1]
                print filename
                l = getList(filename)
                TEMPLATE = html.getTemplate()
                tmpl = web.template.Template(TEMPLATE)
                return tmpl(l)
                #return html.getResultPage(l)
                
        else:
            return html.getDefaultHTML()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
