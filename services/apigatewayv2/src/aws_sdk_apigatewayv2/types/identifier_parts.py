"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IdentifierParts``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max128
    import aws_sdk_apigatewayv2.types.__string_min1_max20
    import aws_sdk_apigatewayv2.types.__string_min1_max4096
    import aws_sdk_apigatewayv2.types.__string_min1_max50


class IdentifierParts(TypedDict):
    method: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max20.__stringMin1Max20"
    ]
    """<p>The method of the product REST endpoint.</p>"""
    path: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max4096.__stringMin1Max4096"
    ]
    """<p>The path of the product REST endpoint.</p>"""
    rest_api_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max50.__stringMin1Max50"
    ]
    """<p>The REST API ID of the product REST endpoint.</p>"""
    stage: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max128.__stringMin1Max128"
    ]
    """<p>The stage of the product REST endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentifierParts) -> dict:
    out: dict = {}
    if "method" in value:
        out["method"] = value["method"]
    if "path" in value:
        out["path"] = value["path"]
    if "rest_api_id" in value:
        out["restApiId"] = value["rest_api_id"]
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> IdentifierParts:
    out: IdentifierParts = {}  # type: ignore[typeddict-item]
    if "method" in data:
        out["method"] = data["method"]
    if "path" in data:
        out["path"] = data["path"]
    if "restApiId" in data:
        out["rest_api_id"] = data["restApiId"]
    if "stage" in data:
        out["stage"] = data["stage"]
    return out
