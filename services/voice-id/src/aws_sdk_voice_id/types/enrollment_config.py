"""Generated from Smithy shape ``com.amazonaws.voiceid#EnrollmentConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.enrollment_job_fraud_detection_config
    import aws_sdk_voice_id.types.existing_enrollment_action


class EnrollmentConfig(TypedDict):
    existing_enrollment_action: NotRequired[
        "aws_sdk_voice_id.types.existing_enrollment_action.ExistingEnrollmentAction"
    ]
    """<p> The action to take when the specified speaker is already enrolled in the specified domain. The default value is <code>SKIP</code>, which skips the enrollment for the existing speaker. Setting the value to <code>OVERWRITE</code> replaces the existing voice prints and enrollment audio stored for that speaker with new data generated from the latest audio.</p>"""
    fraud_detection_config: NotRequired[
        "aws_sdk_voice_id.types.enrollment_job_fraud_detection_config.EnrollmentJobFraudDetectionConfig"
    ]
    """<p>The fraud detection configuration to use for the speaker enrollment job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentConfig) -> dict:
    out: dict = {}
    if "existing_enrollment_action" in value:
        out["ExistingEnrollmentAction"] = value["existing_enrollment_action"]
    if "fraud_detection_config" in value:
        import aws_sdk_voice_id.types.enrollment_job_fraud_detection_config

        out["FraudDetectionConfig"] = (
            aws_sdk_voice_id.types.enrollment_job_fraud_detection_config.serialize_aws_json_1_0(
                value["fraud_detection_config"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnrollmentConfig:
    out: EnrollmentConfig = {}  # type: ignore[typeddict-item]
    if "ExistingEnrollmentAction" in data:
        out["existing_enrollment_action"] = data["ExistingEnrollmentAction"]
    if "FraudDetectionConfig" in data:
        import aws_sdk_voice_id.types.enrollment_job_fraud_detection_config

        out["fraud_detection_config"] = (
            aws_sdk_voice_id.types.enrollment_job_fraud_detection_config.deserialize_aws_json_1_0(
                data["FraudDetectionConfig"]
            )
        )
    return out
