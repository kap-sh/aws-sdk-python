"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    return cast(SourceType, data)
