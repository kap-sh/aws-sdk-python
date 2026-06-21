"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamEncryptionStatus``."""

from typing import Literal, TypeAlias, cast

DeliveryStreamEncryptionStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "ENABLING_FAILED",
    "DISABLED",
    "DISABLING",
    "DISABLING_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamEncryptionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamEncryptionStatus:
    return cast(DeliveryStreamEncryptionStatus, data)
