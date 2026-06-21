"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceType``."""

from typing import Literal, TypeAlias, cast

DataSourceType: TypeAlias = Literal[
    "ADOBE_ANALYTICS",
    "AMAZON_ELASTICSEARCH",
    "ATHENA",
    "AURORA",
    "AURORA_POSTGRESQL",
    "AWS_IOT_ANALYTICS",
    "GITHUB",
    "JIRA",
    "MARIADB",
    "MYSQL",
    "ORACLE",
    "POSTGRESQL",
    "PRESTO",
    "REDSHIFT",
    "S3",
    "S3_TABLES",
    "SALESFORCE",
    "SERVICENOW",
    "SNOWFLAKE",
    "SPARK",
    "SQLSERVER",
    "TERADATA",
    "TWITTER",
    "TIMESTREAM",
    "AMAZON_OPENSEARCH",
    "EXASOL",
    "DATABRICKS",
    "STARBURST",
    "TRINO",
    "BIGQUERY",
    "GOOGLESHEETS",
    "GOOGLE_DRIVE",
    "CONFLUENCE",
    "SHAREPOINT",
    "ONE_DRIVE",
    "WEB_CRAWLER",
    "S3_KNOWLEDGE_BASE",
    "QBUSINESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    return cast(DataSourceType, data)
