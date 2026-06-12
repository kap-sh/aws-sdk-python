"""Generated from Smithy shape ``com.amazonaws.glue#JdbcMetadataEntry``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

JdbcMetadataEntry: TypeAlias = Literal[
    "COMMENTS",
    "RAWTYPES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMENTS",
        "RAWTYPES",
    )
)


def serialize_aws_json_1_1(value: JdbcMetadataEntry) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JdbcMetadataEntry:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JdbcMetadataEntry value: {data!r}")
    return cast(JdbcMetadataEntry, data)
