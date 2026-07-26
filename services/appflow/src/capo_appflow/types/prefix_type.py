"""Generated from Smithy shape ``com.amazonaws.appflow#PrefixType``."""

from typing import Literal, TypeAlias, cast

PrefixType: TypeAlias = Literal[
    "FILENAME",
    "PATH",
    "PATH_AND_FILENAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrefixType) -> str:
    return value


def deserialize_json(data: str) -> PrefixType:
    return cast(PrefixType, data)
