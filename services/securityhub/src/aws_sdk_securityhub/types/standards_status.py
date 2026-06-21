"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsStatus``."""

from typing import Literal, TypeAlias, cast

StandardsStatus: TypeAlias = Literal[
    "PENDING",
    "READY",
    "FAILED",
    "DELETING",
    "INCOMPLETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsStatus) -> str:
    return value


def deserialize_json(data: str) -> StandardsStatus:
    return cast(StandardsStatus, data)
