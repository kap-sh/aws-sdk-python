"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsControlMode``."""

from typing import Literal, TypeAlias, cast

AttachmentsControlMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentsControlMode) -> str:
    return value


def deserialize_json(data: str) -> AttachmentsControlMode:
    return cast(AttachmentsControlMode, data)
