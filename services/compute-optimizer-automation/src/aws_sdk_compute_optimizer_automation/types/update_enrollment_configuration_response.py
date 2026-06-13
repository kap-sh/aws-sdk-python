"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateEnrollmentConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_compute_optimizer_automation.types.enrollment_status


class UpdateEnrollmentConfigurationResponse(TypedDict):
    status: (
        "aws_sdk_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus"
    )
    """<p> The updated enrollment status. </p>"""
    status_reason: NotRequired["str"]
    """<p> The reason for the updated enrollment status. </p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p> The timestamp when the enrollment configuration was last updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_compute_optimizer_automation.types.enrollment_status

    out["status"] = (
        aws_sdk_compute_optimizer_automation.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

    out["lastUpdatedTimestamp"] = (
        aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentConfigurationResponse:
    out: UpdateEnrollmentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_compute_optimizer_automation.types.enrollment_status

        out["status"] = (
            aws_sdk_compute_optimizer_automation.types.enrollment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnrollmentConfigurationResponse.status required"
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnrollmentConfigurationResponse.last_updated_timestamp required"
        )
    return out
