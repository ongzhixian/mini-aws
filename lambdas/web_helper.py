
class ContentType:
    JSON = "application/json"
    HTML = "text/html"
    TEXT = "text/plain"


def response(content, status_code = 200, content_type = ContentType.HTML):
    return {
        "statusCode": status_code,
        "body": content,
        "headers": {
            "Content-Type": content_type
        }
    }


def html_response(content, status_code = 200, content_type = ContentType.HTML):
    return response(content, status_code, content_type)


def json_response(content, status_code = 200, content_type = ContentType.JSON):
    return response(content, status_code, content_type)


def text_response(content, status_code = 200, content_type = ContentType.TEXT):
    return response(content, status_code, content_type)

