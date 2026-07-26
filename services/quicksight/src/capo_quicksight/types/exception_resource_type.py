"""Generated from Smithy shape ``com.amazonaws.quicksight#ExceptionResourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ExceptionResourceType) -> str:
    return value


def deserialize_json(data: str) -> ExceptionResourceType:
    return cast(ExceptionResourceType, data)
