"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleActionInvokeApi``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128


class RoutingRuleActionInvokeApi(TypedDict):
    api_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    stage: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    strip_base_path: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>The strip base path setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleActionInvokeApi) -> dict:
    out: dict = {}
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "stage" in value:
        out["stage"] = value["stage"]
    if "strip_base_path" in value:
        out["stripBasePath"] = value["strip_base_path"]
    return out


def deserialize_json(data: dict) -> RoutingRuleActionInvokeApi:
    out: RoutingRuleActionInvokeApi = {}  # type: ignore[typeddict-item]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    if "stage" in data:
        out["stage"] = data["stage"]
    if "stripBasePath" in data:
        out["strip_base_path"] = data["stripBasePath"]
    return out
