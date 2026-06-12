"""Generated from Smithy shape ``com.amazonaws.databrew#StatisticList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.statistic

StatisticList: TypeAlias = list["aws_sdk_databrew.types.statistic.Statistic"]


# --- restJson1 ser/de ---
def serialize_json(value: StatisticList) -> list:
    return list(value)


def deserialize_json(data: list) -> StatisticList:
    return list(data)
