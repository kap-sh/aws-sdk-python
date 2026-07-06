"""Generated from Smithy shape ``com.amazonaws.bedrock#StopModelInvocationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_invocation_job_identifier


class StopModelInvocationJobRequest(TypedDict, closed=True):
    job_identifier: "aws_sdk_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier"
    """<p>The Amazon Resource Name (ARN) of the batch inference job to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopModelInvocationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopModelInvocationJobRequest:
    out: StopModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
    return out
