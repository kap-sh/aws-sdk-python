"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RetryPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.maximum_event_age_in_seconds
    import aws_sdk_cloudwatch_events.types.maximum_retry_attempts


class RetryPolicy(TypedDict):
    maximum_retry_attempts: NotRequired[
        "aws_sdk_cloudwatch_events.types.maximum_retry_attempts.MaximumRetryAttempts"
    ]
    """<p>The maximum number of retry attempts to make before the request fails. Retry attempts continue until either the maximum number of attempts is made or until the duration of the <code>MaximumEventAgeInSeconds</code> is met.</p>"""
    maximum_event_age_in_seconds: NotRequired[
        "aws_sdk_cloudwatch_events.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
    ]
    """<p>The maximum amount of time, in seconds, to continue to make retry attempts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryPolicy) -> dict:
    out: dict = {}
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "maximum_event_age_in_seconds" in value:
        out["MaximumEventAgeInSeconds"] = value["maximum_event_age_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryPolicy:
    out: RetryPolicy = {}  # type: ignore[typeddict-item]
    if "MaximumRetryAttempts" in data:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    if "MaximumEventAgeInSeconds" in data:
        out["maximum_event_age_in_seconds"] = data["MaximumEventAgeInSeconds"]
    return out
