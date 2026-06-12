"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteModelRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    model_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the model to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteModelRequest:
    out: DeleteModelRequest = {}  # type: ignore[typeddict-item]
    return out
