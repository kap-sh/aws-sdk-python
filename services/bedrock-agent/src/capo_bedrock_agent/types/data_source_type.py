"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceType``."""

from typing import Literal, TypeAlias, cast

DataSourceType: TypeAlias = Literal[
    "S3",
    "WEB",
    "CONFLUENCE",
    "SALESFORCE",
    "SHAREPOINT",
    "CUSTOM",
    "REDSHIFT_METADATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    return cast(DataSourceType, data)
