"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GlueConnectionType: TypeAlias = Literal[
    "SNOWFLAKE",
    "BIGQUERY",
    "DOCUMENTDB",
    "DYNAMODB",
    "MYSQL",
    "OPENSEARCH",
    "ORACLE",
    "POSTGRESQL",
    "REDSHIFT",
    "SAPHANA",
    "SQLSERVER",
    "TERADATA",
    "VERTICA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SNOWFLAKE",
        "BIGQUERY",
        "DOCUMENTDB",
        "DYNAMODB",
        "MYSQL",
        "OPENSEARCH",
        "ORACLE",
        "POSTGRESQL",
        "REDSHIFT",
        "SAPHANA",
        "SQLSERVER",
        "TERADATA",
        "VERTICA",
    )
)


def serialize_json(value: GlueConnectionType) -> str:
    return value


def deserialize_json(data: str) -> GlueConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlueConnectionType value: {data!r}")
    return cast(GlueConnectionType, data)
