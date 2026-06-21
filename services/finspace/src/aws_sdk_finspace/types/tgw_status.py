"""Generated from Smithy shape ``com.amazonaws.finspace#tgwStatus``."""

from typing import Literal, TypeAlias, cast

tgwStatus: TypeAlias = Literal[
    "NONE",
    "UPDATE_REQUESTED",
    "UPDATING",
    "FAILED_UPDATE",
    "SUCCESSFULLY_UPDATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: tgwStatus) -> str:
    return value


def deserialize_json(data: str) -> tgwStatus:
    return cast(tgwStatus, data)
