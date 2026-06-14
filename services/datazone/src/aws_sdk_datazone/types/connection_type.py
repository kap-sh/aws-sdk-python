"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ConnectionType: TypeAlias = Literal[
    "ATHENA",
    "BIGQUERY",
    "DATABRICKS",
    "DOCUMENTDB",
    "DYNAMODB",
    "HYPERPOD",
    "IAM",
    "MYSQL",
    "OPENSEARCH",
    "ORACLE",
    "POSTGRESQL",
    "REDSHIFT",
    "S3",
    "SAPHANA",
    "SNOWFLAKE",
    "SPARK",
    "SQLSERVER",
    "TERADATA",
    "VERTICA",
    "WORKFLOWS_MWAA",
    "AMAZON_Q",
    "MLFLOW",
    "VPC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATHENA",
        "BIGQUERY",
        "DATABRICKS",
        "DOCUMENTDB",
        "DYNAMODB",
        "HYPERPOD",
        "IAM",
        "MYSQL",
        "OPENSEARCH",
        "ORACLE",
        "POSTGRESQL",
        "REDSHIFT",
        "S3",
        "SAPHANA",
        "SNOWFLAKE",
        "SPARK",
        "SQLSERVER",
        "TERADATA",
        "VERTICA",
        "WORKFLOWS_MWAA",
        "AMAZON_Q",
        "MLFLOW",
        "VPC",
    )
)


def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)
