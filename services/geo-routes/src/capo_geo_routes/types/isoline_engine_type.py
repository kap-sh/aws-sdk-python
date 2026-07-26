"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineEngineType``."""

from typing import Literal, TypeAlias, cast

IsolineEngineType: TypeAlias = Literal[
    "Electric",
    "InternalCombustion",
    "PluginHybrid",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineEngineType) -> str:
    return value


def deserialize_json(data: str) -> IsolineEngineType:
    return cast(IsolineEngineType, data)
