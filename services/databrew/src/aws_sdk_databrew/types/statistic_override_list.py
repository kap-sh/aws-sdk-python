"""Generated from Smithy shape ``com.amazonaws.databrew#StatisticOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.statistic_override

StatisticOverrideList: TypeAlias = list[
    "aws_sdk_databrew.types.statistic_override.StatisticOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatisticOverrideList) -> list:
    import aws_sdk_databrew.types.statistic_override

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.statistic_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatisticOverrideList:
    import aws_sdk_databrew.types.statistic_override

    out: StatisticOverrideList = []
    for item in data:
        out.append(aws_sdk_databrew.types.statistic_override.deserialize_json(item))
    return out
