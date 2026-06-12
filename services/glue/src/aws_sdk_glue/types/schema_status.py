"""Generated from Smithy shape ``com.amazonaws.glue#SchemaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SchemaStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: SchemaStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaStatus value: {data!r}")
    return cast(SchemaStatus, data)
