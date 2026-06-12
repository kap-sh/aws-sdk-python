"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataSourceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DataSourceName: TypeAlias = Literal[
    "SalesforceGenie",
    "Snowflake",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SalesforceGenie",
        "Snowflake",
    )
)


def serialize_aws_json_1_1(value: DataSourceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceName value: {data!r}")
    return cast(DataSourceName, data)
