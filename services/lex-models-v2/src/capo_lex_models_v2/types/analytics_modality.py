"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsModality``."""

from typing import Literal, TypeAlias, cast

AnalyticsModality: TypeAlias = Literal[
    "Speech",
    "Text",
    "DTMF",
    "MultiMode",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsModality) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsModality:
    return cast(AnalyticsModality, data)
