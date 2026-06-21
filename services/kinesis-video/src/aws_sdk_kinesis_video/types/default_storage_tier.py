"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DefaultStorageTier``."""

from typing import Literal, TypeAlias, cast

DefaultStorageTier: TypeAlias = Literal[
    "HOT",
    "WARM",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultStorageTier) -> str:
    return value


def deserialize_json(data: str) -> DefaultStorageTier:
    return cast(DefaultStorageTier, data)
