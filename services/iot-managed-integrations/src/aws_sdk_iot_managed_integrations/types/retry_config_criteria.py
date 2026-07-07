"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RetryConfigCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.min_number_of_retries
    import aws_sdk_iot_managed_integrations.types.retry_criteria_failure_type


class RetryConfigCriteria(TypedDict, closed=True):
    failure_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.retry_criteria_failure_type.RetryCriteriaFailureType"
    ]
    """<p>Over-the-air (OTA) retry criteria failure type.</p>"""
    min_number_of_retries: NotRequired[
        "aws_sdk_iot_managed_integrations.types.min_number_of_retries.MinNumberOfRetries"
    ]
    """<p>The number of retries allowed for a failure type for the over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryConfigCriteria) -> dict:
    out: dict = {}
    if "failure_type" in value:
        import aws_sdk_iot_managed_integrations.types.retry_criteria_failure_type

        out["FailureType"] = (
            aws_sdk_iot_managed_integrations.types.retry_criteria_failure_type.serialize_json(
                value["failure_type"]
            )
        )
    if "min_number_of_retries" in value:
        out["MinNumberOfRetries"] = value["min_number_of_retries"]
    return out


def deserialize_json(data: dict) -> RetryConfigCriteria:
    out: RetryConfigCriteria = {}  # type: ignore[typeddict-item]
    if "FailureType" in data:
        import aws_sdk_iot_managed_integrations.types.retry_criteria_failure_type

        out["failure_type"] = (
            aws_sdk_iot_managed_integrations.types.retry_criteria_failure_type.deserialize_json(
                data["FailureType"]
            )
        )
    if "MinNumberOfRetries" in data:
        out["min_number_of_retries"] = data["MinNumberOfRetries"]
    return out
