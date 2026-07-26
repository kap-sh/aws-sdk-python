"""Generated from Smithy shape ``com.amazonaws.connect#InitiateAs``."""

from typing import Literal, TypeAlias, cast

InitiateAs: TypeAlias = Literal[
    "CONNECTED_TO_USER",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InitiateAs) -> str:
    return value


def deserialize_json(data: str) -> InitiateAs:
    return cast(InitiateAs, data)
