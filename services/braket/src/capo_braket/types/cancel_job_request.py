"""Generated from Smithy shape ``com.amazonaws.braket#CancelJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.job_arn


class CancelJobRequest(TypedDict, closed=True):
    job_arn: "capo_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    return out
