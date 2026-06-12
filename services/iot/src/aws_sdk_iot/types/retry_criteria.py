"""Generated from Smithy shape ``com.amazonaws.iot#RetryCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.number_of_retries
    import aws_sdk_iot.types.retryable_failure_type


class RetryCriteria(TypedDict):
    failure_type: "aws_sdk_iot.types.retryable_failure_type.RetryableFailureType"
    """<p>The type of job execution failures that can initiate a job retry.</p>"""
    number_of_retries: "aws_sdk_iot.types.number_of_retries.NumberOfRetries"
    """<p>The number of retries allowed for a failure type for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryCriteria) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.retryable_failure_type

    out["failureType"] = aws_sdk_iot.types.retryable_failure_type.serialize_json(
        value["failure_type"]
    )
    out["numberOfRetries"] = value["number_of_retries"]
    return out


def deserialize_json(data: dict) -> RetryCriteria:
    out: RetryCriteria = {}  # type: ignore[typeddict-item]
    if "failureType" in data:
        import aws_sdk_iot.types.retryable_failure_type

        out["failure_type"] = aws_sdk_iot.types.retryable_failure_type.deserialize_json(
            data["failureType"]
        )
    else:
        raise DeserializationError("RetryCriteria.failure_type required")
    if "numberOfRetries" in data:
        out["number_of_retries"] = data["numberOfRetries"]
    else:
        raise DeserializationError("RetryCriteria.number_of_retries required")
    return out
