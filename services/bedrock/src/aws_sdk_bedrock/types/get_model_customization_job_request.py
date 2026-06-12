"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelCustomizationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_customization_job_identifier


class GetModelCustomizationJobRequest(TypedDict):
    job_identifier: "aws_sdk_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier"
    """<p>Identifier for the customization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelCustomizationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelCustomizationJobRequest:
    out: GetModelCustomizationJobRequest = {}  # type: ignore[typeddict-item]
    return out
