"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

DataSourceStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "UPDATING",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "FAILED",
        "UPDATING",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: DataSourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceStatus value: {data!r}")
    return cast(DataSourceStatus, data)
