"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosMeteringMode``."""

from typing import Literal, TypeAlias, cast

"""Choose how the service meters the loudness of your audio."""
Eac3AtmosMeteringMode: TypeAlias = Literal[
    "LEQ_A",
    "ITU_BS_1770_1",
    "ITU_BS_1770_2",
    "ITU_BS_1770_3",
    "ITU_BS_1770_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosMeteringMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosMeteringMode:
    return cast(Eac3AtmosMeteringMode, data)
