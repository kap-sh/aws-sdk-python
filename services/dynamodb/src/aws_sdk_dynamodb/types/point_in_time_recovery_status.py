"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryStatus``."""

from typing import Literal, TypeAlias, cast

PointInTimeRecoveryStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoveryStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PointInTimeRecoveryStatus:
    return cast(PointInTimeRecoveryStatus, data)
