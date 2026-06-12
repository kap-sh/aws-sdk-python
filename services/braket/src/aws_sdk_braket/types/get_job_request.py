"""Generated from Smithy shape ``com.amazonaws.braket#GetJobRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_braket.types.hybrid_job_additional_attribute_names_list
    import aws_sdk_braket.types.job_arn

class GetJobRequest(TypedDict):
    job_arn: "aws_sdk_braket.types.job_arn.JobArn"
    """<p>The ARN of the hybrid job to retrieve.</p>"""
    additional_attribute_names: NotRequired["aws_sdk_braket.types.hybrid_job_additional_attribute_names_list.HybridJobAdditionalAttributeNamesList"]
    """<p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobRequest:
    out: GetJobRequest = {}  # type: ignore[typeddict-item]
    return out