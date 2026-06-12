"""Generated from Smithy shape ``com.amazonaws.glue#PermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

PermissionType: TypeAlias = Literal[
    "COLUMN_PERMISSION",
    "CELL_FILTER_PERMISSION",
    "NESTED_PERMISSION",
    "NESTED_CELL_PERMISSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLUMN_PERMISSION",
        "CELL_FILTER_PERMISSION",
        "NESTED_PERMISSION",
        "NESTED_CELL_PERMISSION",
    )
)


def serialize_aws_json_1_1(value: PermissionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionType value: {data!r}")
    return cast(PermissionType, data)
