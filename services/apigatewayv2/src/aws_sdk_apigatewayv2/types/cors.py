"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Cors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.cors_header_list
    import aws_sdk_apigatewayv2.types.cors_method_list
    import aws_sdk_apigatewayv2.types.cors_origin_list
    import aws_sdk_apigatewayv2.types.integer_with_length_between_minus1_and86400


class Cors(TypedDict, closed=True):
    allow_credentials: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.</p>"""
    allow_headers: NotRequired[
        "aws_sdk_apigatewayv2.types.cors_header_list.CorsHeaderList"
    ]
    """<p>Represents a collection of allowed headers. Supported only for HTTP APIs.</p>"""
    allow_methods: NotRequired[
        "aws_sdk_apigatewayv2.types.cors_method_list.CorsMethodList"
    ]
    """<p>Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.</p>"""
    allow_origins: NotRequired[
        "aws_sdk_apigatewayv2.types.cors_origin_list.CorsOriginList"
    ]
    """<p>Represents a collection of allowed origins. Supported only for HTTP APIs.</p>"""
    expose_headers: NotRequired[
        "aws_sdk_apigatewayv2.types.cors_header_list.CorsHeaderList"
    ]
    """<p>Represents a collection of exposed headers. Supported only for HTTP APIs.</p>"""
    max_age: NotRequired[
        "aws_sdk_apigatewayv2.types.integer_with_length_between_minus1_and86400.IntegerWithLengthBetweenMinus1And86400"
    ]
    """<p>The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cors) -> dict:
    out: dict = {}
    if "allow_credentials" in value:
        out["allowCredentials"] = value["allow_credentials"]
    if "allow_headers" in value:
        import aws_sdk_apigatewayv2.types.cors_header_list

        out["allowHeaders"] = (
            aws_sdk_apigatewayv2.types.cors_header_list.serialize_json(
                value["allow_headers"]
            )
        )
    if "allow_methods" in value:
        import aws_sdk_apigatewayv2.types.cors_method_list

        out["allowMethods"] = (
            aws_sdk_apigatewayv2.types.cors_method_list.serialize_json(
                value["allow_methods"]
            )
        )
    if "allow_origins" in value:
        import aws_sdk_apigatewayv2.types.cors_origin_list

        out["allowOrigins"] = (
            aws_sdk_apigatewayv2.types.cors_origin_list.serialize_json(
                value["allow_origins"]
            )
        )
    if "expose_headers" in value:
        import aws_sdk_apigatewayv2.types.cors_header_list

        out["exposeHeaders"] = (
            aws_sdk_apigatewayv2.types.cors_header_list.serialize_json(
                value["expose_headers"]
            )
        )
    if "max_age" in value:
        out["maxAge"] = value["max_age"]
    return out


def deserialize_json(data: dict) -> Cors:
    out: Cors = {}  # type: ignore[typeddict-item]
    if "allowCredentials" in data:
        out["allow_credentials"] = data["allowCredentials"]
    if "allowHeaders" in data:
        import aws_sdk_apigatewayv2.types.cors_header_list

        out["allow_headers"] = (
            aws_sdk_apigatewayv2.types.cors_header_list.deserialize_json(
                data["allowHeaders"]
            )
        )
    if "allowMethods" in data:
        import aws_sdk_apigatewayv2.types.cors_method_list

        out["allow_methods"] = (
            aws_sdk_apigatewayv2.types.cors_method_list.deserialize_json(
                data["allowMethods"]
            )
        )
    if "allowOrigins" in data:
        import aws_sdk_apigatewayv2.types.cors_origin_list

        out["allow_origins"] = (
            aws_sdk_apigatewayv2.types.cors_origin_list.deserialize_json(
                data["allowOrigins"]
            )
        )
    if "exposeHeaders" in data:
        import aws_sdk_apigatewayv2.types.cors_header_list

        out["expose_headers"] = (
            aws_sdk_apigatewayv2.types.cors_header_list.deserialize_json(
                data["exposeHeaders"]
            )
        )
    if "maxAge" in data:
        out["max_age"] = data["maxAge"]
    return out
