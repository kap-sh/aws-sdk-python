"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "WEB",
        "CONFLUENCE",
        "SALESFORCE",
        "SHAREPOINT",
        "CUSTOM",
        "REDSHIFT_METADATA",
    )
)


def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceType value: {data!r}")
    return cast(DataSourceType, data)
