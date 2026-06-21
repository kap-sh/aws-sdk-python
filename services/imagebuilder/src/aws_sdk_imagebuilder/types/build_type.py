"""Generated from Smithy shape ``com.amazonaws.imagebuilder#BuildType``."""

from typing import Literal, TypeAlias, cast

BuildType: TypeAlias = Literal[
    "USER_INITIATED",
    "SCHEDULED",
    "IMPORT",
    "IMPORT_ISO",
]


# --- restJson1 ser/de ---
def serialize_json(value: BuildType) -> str:
    return value


def deserialize_json(data: str) -> BuildType:
    return cast(BuildType, data)
