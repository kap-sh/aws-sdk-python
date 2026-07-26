"""Generated from Smithy shape ``com.amazonaws.medialive#Av1Level``."""

from typing import Literal, TypeAlias, cast

"""Av1 Level"""
Av1Level: TypeAlias = Literal[
    "AV1_LEVEL_2",
    "AV1_LEVEL_2_1",
    "AV1_LEVEL_3",
    "AV1_LEVEL_3_1",
    "AV1_LEVEL_4",
    "AV1_LEVEL_4_1",
    "AV1_LEVEL_5",
    "AV1_LEVEL_5_1",
    "AV1_LEVEL_5_2",
    "AV1_LEVEL_5_3",
    "AV1_LEVEL_6",
    "AV1_LEVEL_6_1",
    "AV1_LEVEL_6_2",
    "AV1_LEVEL_6_3",
    "AV1_LEVEL_AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1Level) -> str:
    return value


def deserialize_json(data: str) -> Av1Level:
    return cast(Av1Level, data)
