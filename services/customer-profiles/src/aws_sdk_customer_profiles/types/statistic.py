"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Statistic``."""

from typing import Literal, TypeAlias, cast

Statistic: TypeAlias = Literal[
    "FIRST_OCCURRENCE",
    "LAST_OCCURRENCE",
    "COUNT",
    "SUM",
    "MINIMUM",
    "MAXIMUM",
    "AVERAGE",
    "MAX_OCCURRENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Statistic) -> str:
    return value


def deserialize_json(data: str) -> Statistic:
    return cast(Statistic, data)
