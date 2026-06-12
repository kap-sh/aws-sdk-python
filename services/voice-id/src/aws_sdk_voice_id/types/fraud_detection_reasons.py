"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudDetectionReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.fraud_detection_reason

FraudDetectionReasons: TypeAlias = list[
    "aws_sdk_voice_id.types.fraud_detection_reason.FraudDetectionReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudDetectionReasons) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FraudDetectionReasons:
    return list(data)
