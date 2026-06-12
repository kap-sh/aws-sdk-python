"""Generated from Smithy shape ``com.amazonaws.glue#JDBCDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

JDBCDataType: TypeAlias = Literal[
    "ARRAY",
    "BIGINT",
    "BINARY",
    "BIT",
    "BLOB",
    "BOOLEAN",
    "CHAR",
    "CLOB",
    "DATALINK",
    "DATE",
    "DECIMAL",
    "DISTINCT",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "JAVA_OBJECT",
    "LONGNVARCHAR",
    "LONGVARBINARY",
    "LONGVARCHAR",
    "NCHAR",
    "NCLOB",
    "NULL",
    "NUMERIC",
    "NVARCHAR",
    "OTHER",
    "REAL",
    "REF",
    "REF_CURSOR",
    "ROWID",
    "SMALLINT",
    "SQLXML",
    "STRUCT",
    "TIME",
    "TIME_WITH_TIMEZONE",
    "TIMESTAMP",
    "TIMESTAMP_WITH_TIMEZONE",
    "TINYINT",
    "VARBINARY",
    "VARCHAR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARRAY",
        "BIGINT",
        "BINARY",
        "BIT",
        "BLOB",
        "BOOLEAN",
        "CHAR",
        "CLOB",
        "DATALINK",
        "DATE",
        "DECIMAL",
        "DISTINCT",
        "DOUBLE",
        "FLOAT",
        "INTEGER",
        "JAVA_OBJECT",
        "LONGNVARCHAR",
        "LONGVARBINARY",
        "LONGVARCHAR",
        "NCHAR",
        "NCLOB",
        "NULL",
        "NUMERIC",
        "NVARCHAR",
        "OTHER",
        "REAL",
        "REF",
        "REF_CURSOR",
        "ROWID",
        "SMALLINT",
        "SQLXML",
        "STRUCT",
        "TIME",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP",
        "TIMESTAMP_WITH_TIMEZONE",
        "TINYINT",
        "VARBINARY",
        "VARCHAR",
    )
)


def serialize_aws_json_1_1(value: JDBCDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JDBCDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JDBCDataType value: {data!r}")
    return cast(JDBCDataType, data)
