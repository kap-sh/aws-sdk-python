"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenWatermarksCbetStepaside``."""

from typing import Literal, TypeAlias, cast

"""Nielsen Watermarks Cbet Stepaside"""
NielsenWatermarksCbetStepaside: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NielsenWatermarksCbetStepaside) -> str:
    return value


def deserialize_json(data: str) -> NielsenWatermarksCbetStepaside:
    return cast(NielsenWatermarksCbetStepaside, data)
