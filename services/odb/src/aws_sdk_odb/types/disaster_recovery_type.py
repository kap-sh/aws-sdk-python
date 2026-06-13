"""Generated from Smithy shape ``com.amazonaws.odb#DisasterRecoveryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DisasterRecoveryType: TypeAlias = Literal[
    "ADG",
    "BACKUP_BASED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADG",
        "BACKUP_BASED",
    )
)


def serialize_aws_json_1_0(value: DisasterRecoveryType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DisasterRecoveryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DisasterRecoveryType value: {data!r}")
    return cast(DisasterRecoveryType, data)
