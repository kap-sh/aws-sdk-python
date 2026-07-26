"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceType``."""

from typing import Literal, TypeAlias, cast

DataSourceType: TypeAlias = Literal[
    "S3",
    "SHAREPOINT",
    "DATABASE",
    "SALESFORCE",
    "ONEDRIVE",
    "SERVICENOW",
    "CUSTOM",
    "CONFLUENCE",
    "GOOGLEDRIVE",
    "WEBCRAWLER",
    "WORKDOCS",
    "FSX",
    "SLACK",
    "BOX",
    "QUIP",
    "JIRA",
    "GITHUB",
    "ALFRESCO",
    "TEMPLATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceType:
    return cast(DataSourceType, data)
