"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InventoryDeletionStatus: TypeAlias = Literal[
    "InProgress",
    "Complete",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Complete",
    )
)


def serialize_aws_json_1_1(value: InventoryDeletionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryDeletionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InventoryDeletionStatus value: {data!r}")
    return cast(InventoryDeletionStatus, data)
