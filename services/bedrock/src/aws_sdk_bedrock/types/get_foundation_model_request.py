"""Generated from Smithy shape ``com.amazonaws.bedrock#GetFoundationModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.get_foundation_model_identifier


class GetFoundationModelRequest(TypedDict):
    model_identifier: "aws_sdk_bedrock.types.get_foundation_model_identifier.GetFoundationModelIdentifier"
    """<p>The model identifier. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFoundationModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFoundationModelRequest:
    out: GetFoundationModelRequest = {}  # type: ignore[typeddict-item]
    return out
