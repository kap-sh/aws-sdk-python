"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointDisplayContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.__string_min1_max1024
    import aws_sdk_apigatewayv2.types.__string_min1_max32768


class EndpointDisplayContentResponse(TypedDict, closed=True):
    body: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max32768.__stringMin1Max32768"
    ]
    """<p>The API documentation.</p>"""
    endpoint: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max1024.__stringMin1Max1024"
    ]
    """<p>The URL to invoke your REST API.</p>"""
    operation_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
    ]
    """<p>The operation name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDisplayContentResponse) -> dict:
    out: dict = {}
    if "body" in value:
        out["body"] = value["body"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "operation_name" in value:
        out["operationName"] = value["operation_name"]
    return out


def deserialize_json(data: dict) -> EndpointDisplayContentResponse:
    out: EndpointDisplayContentResponse = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "operationName" in data:
        out["operation_name"] = data["operationName"]
    return out
