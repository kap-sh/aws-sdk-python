"""Generated from Smithy shape ``com.amazonaws.auditmanager#ShareRequestAction``."""

from typing import Literal, TypeAlias, cast

ShareRequestAction: TypeAlias = Literal[
    "ACCEPT",
    "DECLINE",
    "REVOKE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareRequestAction) -> str:
    return value


def deserialize_json(data: str) -> ShareRequestAction:
    return cast(ShareRequestAction, data)
