"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateApiMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.selection_key
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128


class UpdateApiMappingRequest(TypedDict):
    api_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>The API identifier.</p>"""
    api_mapping_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API mapping identifier.</p>"""
    api_mapping_key: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
    ]
    """<p>The API mapping key.</p>"""
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    stage: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The API stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiMappingRequest) -> dict:
    out: dict = {}
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "api_mapping_key" in value:
        out["apiMappingKey"] = value["api_mapping_key"]
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> UpdateApiMappingRequest:
    out: UpdateApiMappingRequest = {}  # type: ignore[typeddict-item]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    if "apiMappingKey" in data:
        out["api_mapping_key"] = data["apiMappingKey"]
    if "stage" in data:
        out["stage"] = data["stage"]
    return out
