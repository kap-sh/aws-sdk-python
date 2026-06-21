"""Generated from Smithy shape ``com.amazonaws.auditmanager#ShareRequestType``."""

from typing import Literal, TypeAlias, cast

ShareRequestType: TypeAlias = Literal[
    "SENT",
    "RECEIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareRequestType) -> str:
    return value


def deserialize_json(data: str) -> ShareRequestType:
    return cast(ShareRequestType, data)
