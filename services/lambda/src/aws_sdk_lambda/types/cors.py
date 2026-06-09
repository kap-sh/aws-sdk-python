"""Generated from Smithy shape ``com.amazonaws.lambda#Cors``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.allow_credentials
    import aws_sdk_lambda.types.allow_methods_list
    import aws_sdk_lambda.types.allow_origins_list
    import aws_sdk_lambda.types.headers_list
    import aws_sdk_lambda.types.max_age


class Cors(TypedDict):
    allow_credentials: NotRequired[
        "aws_sdk_lambda.types.allow_credentials.AllowCredentials"
    ]
    """<p>Whether to allow cookies or other credentials in requests to your function URL. The default is <code>false</code>.</p>"""
    allow_headers: NotRequired["aws_sdk_lambda.types.headers_list.HeadersList"]
    """<p>The HTTP headers that origins can include in requests to your function URL. For example: <code>Date</code>, <code>Keep-Alive</code>, <code>X-Custom-Header</code>.</p>"""
    allow_methods: NotRequired[
        "aws_sdk_lambda.types.allow_methods_list.AllowMethodsList"
    ]
    """<p>The HTTP methods that are allowed when calling your function URL. For example: <code>GET</code>, <code>POST</code>, <code>DELETE</code>, or the wildcard character (<code>*</code>).</p>"""
    allow_origins: NotRequired[
        "aws_sdk_lambda.types.allow_origins_list.AllowOriginsList"
    ]
    """<p>The origins that can access your function URL. You can list any number of specific origins, separated by a comma. For example: <code>https://www.example.com</code>, <code>http://localhost:60905</code>.</p> <p>Alternatively, you can grant access to all origins using the wildcard character (<code>*</code>).</p>"""
    expose_headers: NotRequired["aws_sdk_lambda.types.headers_list.HeadersList"]
    """<p>The HTTP headers in your function response that you want to expose to origins that call your function URL. For example: <code>Date</code>, <code>Keep-Alive</code>, <code>X-Custom-Header</code>.</p>"""
    max_age: NotRequired["aws_sdk_lambda.types.max_age.MaxAge"]
    """<p>The maximum amount of time, in seconds, that web browsers can cache results of a preflight request. By default, this is set to <code>0</code>, which means that the browser doesn't cache results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cors) -> dict:
    out: dict = {}
    if "allow_credentials" in value:
        out["AllowCredentials"] = value["allow_credentials"]
    if "allow_headers" in value:
        import aws_sdk_lambda.types.headers_list

        out["AllowHeaders"] = aws_sdk_lambda.types.headers_list.serialize_json(
            value["allow_headers"]
        )
    if "allow_methods" in value:
        import aws_sdk_lambda.types.allow_methods_list

        out["AllowMethods"] = aws_sdk_lambda.types.allow_methods_list.serialize_json(
            value["allow_methods"]
        )
    if "allow_origins" in value:
        import aws_sdk_lambda.types.allow_origins_list

        out["AllowOrigins"] = aws_sdk_lambda.types.allow_origins_list.serialize_json(
            value["allow_origins"]
        )
    if "expose_headers" in value:
        import aws_sdk_lambda.types.headers_list

        out["ExposeHeaders"] = aws_sdk_lambda.types.headers_list.serialize_json(
            value["expose_headers"]
        )
    if "max_age" in value:
        out["MaxAge"] = value["max_age"]
    return out


def deserialize_json(data: dict) -> Cors:
    out: Cors = {}  # type: ignore[typeddict-item]
    if "AllowCredentials" in data:
        out["allow_credentials"] = data["AllowCredentials"]
    if "AllowHeaders" in data:
        import aws_sdk_lambda.types.headers_list

        out["allow_headers"] = aws_sdk_lambda.types.headers_list.deserialize_json(
            data["AllowHeaders"]
        )
    if "AllowMethods" in data:
        import aws_sdk_lambda.types.allow_methods_list

        out["allow_methods"] = aws_sdk_lambda.types.allow_methods_list.deserialize_json(
            data["AllowMethods"]
        )
    if "AllowOrigins" in data:
        import aws_sdk_lambda.types.allow_origins_list

        out["allow_origins"] = aws_sdk_lambda.types.allow_origins_list.deserialize_json(
            data["AllowOrigins"]
        )
    if "ExposeHeaders" in data:
        import aws_sdk_lambda.types.headers_list

        out["expose_headers"] = aws_sdk_lambda.types.headers_list.deserialize_json(
            data["ExposeHeaders"]
        )
    if "MaxAge" in data:
        out["max_age"] = data["MaxAge"]
    return out
