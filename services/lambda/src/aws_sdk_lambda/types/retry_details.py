"""Generated from Smithy shape ``com.amazonaws.lambda#RetryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.attempt_count
    import aws_sdk_lambda.types.duration_seconds


class RetryDetails(TypedDict, closed=True):
    current_attempt: "aws_sdk_lambda.types.attempt_count.AttemptCount"
    """<p>The current attempt number for this operation.</p>"""
    next_attempt_delay_seconds: NotRequired[
        "aws_sdk_lambda.types.duration_seconds.DurationSeconds"
    ]
    """<p>The delay before the next retry attempt, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryDetails) -> dict:
    out: dict = {}
    out["CurrentAttempt"] = value.get("current_attempt", 0)
    if "next_attempt_delay_seconds" in value:
        out["NextAttemptDelaySeconds"] = value["next_attempt_delay_seconds"]
    return out


def deserialize_json(data: dict) -> RetryDetails:
    out: RetryDetails = {}  # type: ignore[typeddict-item]
    if "CurrentAttempt" in data:
        out["current_attempt"] = data["CurrentAttempt"]
    else:
        out["current_attempt"] = 0
    if "NextAttemptDelaySeconds" in data:
        out["next_attempt_delay_seconds"] = data["NextAttemptDelaySeconds"]
    return out
