"""Generated from Smithy shape ``com.amazonaws.pipes#BatchRetryStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.batch_retry_attempts


class BatchRetryStrategy(TypedDict, closed=True):
    attempts: NotRequired["aws_sdk_pipes.types.batch_retry_attempts.BatchRetryAttempts"]
    """<p>The number of times to move a job to the <code>RUNNABLE</code> status. If the value of <code>attempts</code> is greater than one, the job is retried on failure the same number of attempts as the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRetryStrategy) -> dict:
    out: dict = {}
    if "attempts" in value:
        out["Attempts"] = value["attempts"]
    return out


def deserialize_json(data: dict) -> BatchRetryStrategy:
    out: BatchRetryStrategy = {}  # type: ignore[typeddict-item]
    if "Attempts" in data:
        out["attempts"] = data["Attempts"]
    return out
