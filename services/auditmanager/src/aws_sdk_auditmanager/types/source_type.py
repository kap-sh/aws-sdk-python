"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "AWS_Cloudtrail",
    "AWS_Config",
    "AWS_Security_Hub",
    "AWS_API_Call",
    "MANUAL",
    "Common_Control",
    "Core_Control",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_Cloudtrail",
        "AWS_Config",
        "AWS_Security_Hub",
        "AWS_API_Call",
        "MANUAL",
        "Common_Control",
        "Core_Control",
    )
)


def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
