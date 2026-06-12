"""Generated from Smithy shape ``com.amazonaws.bedrock#GetInferenceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_identifier


class GetInferenceProfileRequest(TypedDict):
    inference_profile_identifier: (
        "aws_sdk_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier"
    )
    """<p>The ID or Amazon Resource Name (ARN) of the inference profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInferenceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInferenceProfileRequest:
    out: GetInferenceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
