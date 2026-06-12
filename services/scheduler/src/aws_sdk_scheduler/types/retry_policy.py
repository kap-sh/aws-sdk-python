"""Generated from Smithy shape ``com.amazonaws.scheduler#RetryPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.maximum_event_age_in_seconds
    import aws_sdk_scheduler.types.maximum_retry_attempts


class RetryPolicy(TypedDict):
    maximum_event_age_in_seconds: NotRequired[
        "aws_sdk_scheduler.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
    ]
    """<p>The maximum amount of time, in seconds, to continue to make retry attempts.</p>"""
    maximum_retry_attempts: NotRequired[
        "aws_sdk_scheduler.types.maximum_retry_attempts.MaximumRetryAttempts"
    ]
    """<p>The maximum number of retry attempts to make before the request fails. Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the <code>MaximumEventAgeInSeconds</code> is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryPolicy) -> dict:
    out: dict = {}
    if "maximum_event_age_in_seconds" in value:
        out["MaximumEventAgeInSeconds"] = value["maximum_event_age_in_seconds"]
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    return out


def deserialize_json(data: dict) -> RetryPolicy:
    out: RetryPolicy = {}  # type: ignore[typeddict-item]
    if "MaximumEventAgeInSeconds" in data:
        out["maximum_event_age_in_seconds"] = data["MaximumEventAgeInSeconds"]
    if "MaximumRetryAttempts" in data:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    return out
