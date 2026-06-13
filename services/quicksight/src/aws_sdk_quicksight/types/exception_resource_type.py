"""Generated from Smithy shape ``com.amazonaws.quicksight#ExceptionResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ExceptionResourceType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "NAMESPACE",
    "ACCOUNT_SETTINGS",
    "IAMPOLICY_ASSIGNMENT",
    "DATA_SOURCE",
    "DATA_SET",
    "VPC_CONNECTION",
    "INGESTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
        "NAMESPACE",
        "ACCOUNT_SETTINGS",
        "IAMPOLICY_ASSIGNMENT",
        "DATA_SOURCE",
        "DATA_SET",
        "VPC_CONNECTION",
        "INGESTION",
    )
)


def serialize_json(value: ExceptionResourceType) -> str:
    return value


def deserialize_json(data: str) -> ExceptionResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExceptionResourceType value: {data!r}")
    return cast(ExceptionResourceType, data)
