"""Generated from Smithy shape ``com.amazonaws.odb#DisasterRecoveryType``."""

from typing import Literal, TypeAlias, cast

DisasterRecoveryType: TypeAlias = Literal[
    "ADG",
    "BACKUP_BASED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisasterRecoveryType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DisasterRecoveryType:
    return cast(DisasterRecoveryType, data)
