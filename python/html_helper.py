import urllib
import datetime
from datetime import timedelta 

class HTMLHelper:
    #start __init__
    def __init__(self):
        self.html = ''
                
    #start getDefaultHTML
    def getDefaultHTML(self, error = 0):
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title>Entity Centric KB Expansion</title>
        <meta name="description" content="A description of your website">
        <meta name="keywords" content="keyword1, keyword2, keyword3">
        <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.4.1/build/cssgrids/grids-min.css" />
        <link rel="stylesheet" type="text/css" href="static/styles.css" />
        <link rel="icon" type="image/png" href="static/favicon.ico">
        </head>
        <body>

		<div id="wrapper"> 

		  <div id="header"> 

            <div class="top_banner">
              <h1> ENTICE <br/> </h1>
              <p>ENTity CEntric KB Expansion</p>
            </div>
           </div>

          <div id="page_content">

            <div class="navigation">
              <ul>
                <li><a href="https://docs.google.com/forms/d/1f1WpQmRi2irETBJILpVZGsq6B8PMBDYD9TykUIV5WdE/viewform?usp=send_form">Feedback</a></li>
              </ul>
            </div>
            <div class="yui3-g" id="doc">
             <div class="yui3-u" id="hd">
                <h2> Specify Entity Name:</h2>
             </div>

              <div class="yui3-u" id="bd">
                <form name="keyform" id="key-form" method="get" onSubmit="return checkEmpty(this);">
                 <p> <input type="text" value="" name="keyword" style="width:20%;" id="keyword"/><br/><input type="submit" value="Submit" id="sub"/> 
                </form>
              </div>
             </div>
            </div>
           </div>
              <script type="text/javascript">
              function checkEmpty(f) {
                if (f.keyword.value === "") {
                    alert('Please enter a valid entity');
                    return false;
                }else{
                    f.submit();
                    return true;
                }
              }
                var _gaq = _gaq || [];
                _gaq.push(['_setAccount', 'UA-31119754-1']);
                _gaq.push(['_trackPageview']);
            
                (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
            </script>
        </div>
        </body>
        </html>
        '''
        return html
        
    def getResultPage(self,resultList):
        result = ''
        #for l in resultList:
        #    result += l + "\n"
        result = "\n".join(resultList)
        print result
        html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Entity Centric KB Expansion</title>
    <meta name="description" content="A description of your website">
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.4.1/build/cssgrids/grids-min.css" />
    <link rel="stylesheet" type="text/css" href="static/styles.css" />
    <link rel="icon" type="image/png" href="static/favicon.ico">
    </head>
    <body>

    <div id="wrapper"> 

      <div id="header"> 

        <div class="top_banner">
          <h1> ENTICE <br/> </h1>
          <p>ENTity CEntric KB Expansion</p>
        </div>
       </div>

      <div id="page_content">

        <div class="navigation">
          <ul>
            <li><a href="create a sheet for feedback">Feedback</a></li>
          </ul>
        </div>
        <div class="yui3-g" id="doc">
        
          <div class="yui3-u" id="bd">
            <form name="resultform" id="result-form" method="get">
   ''' + result +'''
            <br/>
          <button type="back" value="Back" id="back">Back</button> 
          </form>
          </div>
         </div>
        </div>
       </div>
       <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-31119754-1']);
        _gaq.push(['_trackPageview']);
    
        (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
        </script>
        </div>
        </body>
        </html>
        '''
        return html

    def getTemplate(self):
        TEMPLATE = '''$def with(resultList)
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title>Entity Centric KB Expansion</title>
        <meta name="description" content="A description of your website">
        <meta name="keywords" content="keyword1, keyword2, keyword3">
        <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.4.1/build/cssgrids/grids-min.css" />
        <link rel="stylesheet" type="text/css" href="static/styles.css" />
        <link rel="icon" type="image/png" href="static/favicon.ico">
        </head>
        <body>

        <div id="wrapper"> 

          <div id="header"> 

            <div class="top_banner">
              <h1> ENTICE <br/> </h1>
              <p>ENTity CEntric KB Expansion</p>
            </div>
           </div>

          <div id="page_content">

            <div class="navigation">
              <ul>
                <li><a href="create a sheet for feedback">Feedback</a></li>
              </ul>
            </div>
            <div class="yui3-g" id="doc">
            
              <div class="yui3-u" id="bd">
                <form name="resultform" id="result-form" method="get">
		<h2>Results:</h2>
		<table>
		<tr>
		$for i in range(0,len(resultList)):
		<td>$resultList[i]</td><br />
    	
		</tr>
		</table>          
              <br/>
              <button type="back" value="Back" id="back">Back</button> 
              </form>
              </div>
             </div>
            </div>
           </div>
           <script type="text/javascript">
            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-31119754-1']);
            _gaq.push(['_trackPageview']);
        
            (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
            </script>
            </div>
            </body>
            </html>
            '''
        return TEMPLATE
