"""Generated from Smithy shape ``com.amazonaws.databrew#AllowedStatisticList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.allowed_statistics

AllowedStatisticList: TypeAlias = list[
    "capo_databrew.types.allowed_statistics.AllowedStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStatisticList) -> list:
    import capo_databrew.types.allowed_statistics

    out: list = []
    for item in value:
        out.append(capo_databrew.types.allowed_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedStatisticList:
    import capo_databrew.types.allowed_statistics

    out: AllowedStatisticList = []
    for item in data:
        out.append(capo_databrew.types.allowed_statistics.deserialize_json(item))
    return out
