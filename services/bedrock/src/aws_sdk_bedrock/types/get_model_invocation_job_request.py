"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelInvocationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_invocation_job_identifier


class GetModelInvocationJobRequest(TypedDict):
    job_identifier: "aws_sdk_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier"
    """<p>The Amazon Resource Name (ARN) of the batch inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelInvocationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelInvocationJobRequest:
    out: GetModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
    return out
