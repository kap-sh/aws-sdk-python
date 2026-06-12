"""Generated from Smithy shape ``com.amazonaws.memorydb#DataTieringStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

DataTieringStatus: TypeAlias = Literal[
    "true",
    "false",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "true",
        "false",
    )
)


def serialize_aws_json_1_1(value: DataTieringStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataTieringStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataTieringStatus value: {data!r}")
    return cast(DataTieringStatus, data)
