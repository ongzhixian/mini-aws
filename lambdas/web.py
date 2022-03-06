import os
import sys
from jinja2 import Environment, FileSystemLoader
from web_helper import http_response

def lambda_handler(event, context):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "html_templates"), encoding="utf8"))
    # my_name = False
    # if event["queryStringParameters"] and "my_name" in event["queryStringParameters"]:
    #     my_name_query = event["queryStringParameters"]["my_name"]
    template = env.get_template("index.html")
    #html = template.render(my_name=my_name_query)
    html = template.render()
    return http_response(html)


def example_static_content_handler(event, context):
    html = '<html><head><title>HTML from API Gateway/Lambda</title></head><body><h1>HTML from API Gateway/Lambda</h1></body></html>'
    return http_response(html)



