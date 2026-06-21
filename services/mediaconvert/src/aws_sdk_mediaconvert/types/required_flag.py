"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RequiredFlag``."""

from typing import Literal, TypeAlias, cast

"""Set to ENABLED to force a rendition to be included."""
RequiredFlag: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredFlag) -> str:
    return value


def deserialize_json(data: str) -> RequiredFlag:
    return cast(RequiredFlag, data)
