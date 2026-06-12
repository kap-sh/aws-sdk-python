"""Generated from Smithy shape ``com.amazonaws.emrserverless#RetryPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.attempt_number


class RetryPolicy(TypedDict):
    max_attempts: NotRequired[
        "aws_sdk_emr_serverless.types.attempt_number.AttemptNumber"
    ]
    """<p>Maximum number of attempts for the job run. This parameter is only applicable for <code>BATCH</code> mode.</p>"""
    max_failed_attempts_per_hour: NotRequired["int"]
    """<p>Maximum number of failed attempts per hour. This [arameter is only applicable for <code>STREAMING</code> mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryPolicy) -> dict:
    out: dict = {}
    if "max_attempts" in value:
        out["maxAttempts"] = value["max_attempts"]
    if "max_failed_attempts_per_hour" in value:
        out["maxFailedAttemptsPerHour"] = value["max_failed_attempts_per_hour"]
    return out


def deserialize_json(data: dict) -> RetryPolicy:
    out: RetryPolicy = {}  # type: ignore[typeddict-item]
    if "maxAttempts" in data:
        out["max_attempts"] = data["maxAttempts"]
    if "maxFailedAttemptsPerHour" in data:
        out["max_failed_attempts_per_hour"] = data["maxFailedAttemptsPerHour"]
    return out
