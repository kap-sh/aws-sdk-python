"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

UpdateStatus: TypeAlias = Literal[
    "READY",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateStatus:
    return cast(UpdateStatus, data)
