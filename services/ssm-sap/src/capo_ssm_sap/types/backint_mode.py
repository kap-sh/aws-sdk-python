"""Generated from Smithy shape ``com.amazonaws.ssmsap#BackintMode``."""

from typing import Literal, TypeAlias, cast

BackintMode: TypeAlias = Literal["AWSBackup",]


# --- restJson1 ser/de ---
def serialize_json(value: BackintMode) -> str:
    return value


def deserialize_json(data: str) -> BackintMode:
    return cast(BackintMode, data)
