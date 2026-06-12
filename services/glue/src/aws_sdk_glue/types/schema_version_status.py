"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SchemaVersionStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "FAILURE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "FAILURE",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: SchemaVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaVersionStatus value: {data!r}")
    return cast(SchemaVersionStatus, data)
