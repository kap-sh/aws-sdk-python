"""Generated from Smithy shape ``com.amazonaws.eventbridge#BatchRetryStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.integer


class BatchRetryStrategy(TypedDict, closed=True):
    attempts: "aws_sdk_eventbridge.types.integer.Integer"
    """<p>The number of times to attempt to retry, if the job fails. Valid values are 1–10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRetryStrategy) -> dict:
    out: dict = {}
    out["Attempts"] = value.get("attempts", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchRetryStrategy:
    out: BatchRetryStrategy = {}  # type: ignore[typeddict-item]
    if "Attempts" in data:
        out["attempts"] = data["Attempts"]
    else:
        out["attempts"] = 0
    return out
