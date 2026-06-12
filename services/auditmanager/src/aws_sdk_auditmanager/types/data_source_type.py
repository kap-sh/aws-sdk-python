"""Generated from Smithy shape ``com.amazonaws.auditmanager#DataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

DataSourceType: TypeAlias = Literal[
    "AWS_Cloudtrail",
    "AWS_Config",
    "AWS_Security_Hub",
    "AWS_API_Call",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_Cloudtrail",
        "AWS_Config",
        "AWS_Security_Hub",
        "AWS_API_Call",
        "MANUAL",
    )
)


def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceType value: {data!r}")
    return cast(DataSourceType, data)
