"""Generated from Smithy shape ``com.amazonaws.bedrock#GetFoundationModelAvailabilityRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_id


class GetFoundationModelAvailabilityRequest(TypedDict):
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>The model Id of the foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFoundationModelAvailabilityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFoundationModelAvailabilityRequest:
    out: GetFoundationModelAvailabilityRequest = {}  # type: ignore[typeddict-item]
    return out
