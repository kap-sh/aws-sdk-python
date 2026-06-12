"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteStageRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the Stage resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStageRequest:
    out: DeleteStageRequest = {}  # type: ignore[typeddict-item]
    return out
