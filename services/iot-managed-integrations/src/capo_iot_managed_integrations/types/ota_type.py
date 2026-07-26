"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaType``."""

from typing import Literal, TypeAlias, cast

OtaType: TypeAlias = Literal[
    "ONE_TIME",
    "CONTINUOUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: OtaType) -> str:
    return value


def deserialize_json(data: str) -> OtaType:
    return cast(OtaType, data)
