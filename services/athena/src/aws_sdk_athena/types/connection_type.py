"""Generated from Smithy shape ``com.amazonaws.athena#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

ConnectionType: TypeAlias = Literal[
    "DYNAMODB",
    "MYSQL",
    "POSTGRESQL",
    "REDSHIFT",
    "ORACLE",
    "SYNAPSE",
    "SQLSERVER",
    "DB2",
    "OPENSEARCH",
    "BIGQUERY",
    "GOOGLECLOUDSTORAGE",
    "HBASE",
    "DOCUMENTDB",
    "CMDB",
    "TPCDS",
    "TIMESTREAM",
    "SAPHANA",
    "SNOWFLAKE",
    "DATALAKEGEN2",
    "DB2AS400",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DYNAMODB",
        "MYSQL",
        "POSTGRESQL",
        "REDSHIFT",
        "ORACLE",
        "SYNAPSE",
        "SQLSERVER",
        "DB2",
        "OPENSEARCH",
        "BIGQUERY",
        "GOOGLECLOUDSTORAGE",
        "HBASE",
        "DOCUMENTDB",
        "CMDB",
        "TPCDS",
        "TIMESTREAM",
        "SAPHANA",
        "SNOWFLAKE",
        "DATALAKEGEN2",
        "DB2AS400",
    )
)


def serialize_aws_json_1_1(value: ConnectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)
