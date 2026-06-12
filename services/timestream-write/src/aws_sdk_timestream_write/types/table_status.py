"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#TableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

TableStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "RESTORING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
        "RESTORING",
    )
)


def serialize_aws_json_1_0(value: TableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableStatus value: {data!r}")
    return cast(TableStatus, data)
