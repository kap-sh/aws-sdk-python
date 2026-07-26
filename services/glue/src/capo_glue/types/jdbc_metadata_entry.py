"""Generated from Smithy shape ``com.amazonaws.glue#JdbcMetadataEntry``."""

from typing import Literal, TypeAlias, cast

JdbcMetadataEntry: TypeAlias = Literal[
    "COMMENTS",
    "RAWTYPES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JdbcMetadataEntry) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JdbcMetadataEntry:
    return cast(JdbcMetadataEntry, data)
