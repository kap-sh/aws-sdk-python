"""Generated from Smithy shape ``com.amazonaws.databrew#StatisticOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.statistic_override

StatisticOverrideList: TypeAlias = list[
    "capo_databrew.types.statistic_override.StatisticOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatisticOverrideList) -> list:
    import capo_databrew.types.statistic_override

    out: list = []
    for item in value:
        out.append(capo_databrew.types.statistic_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatisticOverrideList:
    import capo_databrew.types.statistic_override

    out: StatisticOverrideList = []
    for item in data:
        out.append(capo_databrew.types.statistic_override.deserialize_json(item))
    return out
