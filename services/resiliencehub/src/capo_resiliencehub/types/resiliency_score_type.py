"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyScoreType``."""

from typing import Literal, TypeAlias, cast

ResiliencyScoreType: TypeAlias = Literal[
    "Compliance",
    "Test",
    "Alarm",
    "Sop",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResiliencyScoreType) -> str:
    return value


def deserialize_json(data: str) -> ResiliencyScoreType:
    return cast(ResiliencyScoreType, data)
