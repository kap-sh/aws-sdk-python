"""Generated from Smithy shape ``com.amazonaws.connect#ResponseMode``."""

from typing import Literal, TypeAlias, cast

ResponseMode: TypeAlias = Literal[
    "INCREMENTAL",
    "COMPLETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseMode) -> str:
    return value


def deserialize_json(data: str) -> ResponseMode:
    return cast(ResponseMode, data)
