"""Generated from Smithy shape ``com.amazonaws.ssm#LastResourceDataSyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

LastResourceDataSyncStatus: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Successful",
        "Failed",
        "InProgress",
    )
)


def serialize_aws_json_1_1(value: LastResourceDataSyncStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastResourceDataSyncStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LastResourceDataSyncStatus value: {data!r}"
        )
    return cast(LastResourceDataSyncStatus, data)
