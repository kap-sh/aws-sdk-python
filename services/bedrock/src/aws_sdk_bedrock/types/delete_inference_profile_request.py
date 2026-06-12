"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteInferenceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_identifier


class DeleteInferenceProfileRequest(TypedDict):
    inference_profile_identifier: (
        "aws_sdk_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) or ID of the application inference profile to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInferenceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInferenceProfileRequest:
    out: DeleteInferenceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
