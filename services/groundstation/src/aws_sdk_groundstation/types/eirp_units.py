"""Generated from Smithy shape ``com.amazonaws.groundstation#EirpUnits``."""

from typing import Literal, TypeAlias, cast

EirpUnits: TypeAlias = Literal["dBW",]


# --- restJson1 ser/de ---
def serialize_json(value: EirpUnits) -> str:
    return value


def deserialize_json(data: str) -> EirpUnits:
    return cast(EirpUnits, data)
