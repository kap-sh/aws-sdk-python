"""Generated from Smithy shape ``com.amazonaws.connect#Statistic``."""

from typing import Literal, TypeAlias, cast

Statistic: TypeAlias = Literal[
    "SUM",
    "MAX",
    "AVG",
]


# --- restJson1 ser/de ---
def serialize_json(value: Statistic) -> str:
    return value


def deserialize_json(data: str) -> Statistic:
    return cast(Statistic, data)
