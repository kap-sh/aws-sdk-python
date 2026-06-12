"""Generated from Smithy shape ``com.amazonaws.apigateway#GetStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetStageRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the Stage resource to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStageRequest:
    out: GetStageRequest = {}  # type: ignore[typeddict-item]
    return out
