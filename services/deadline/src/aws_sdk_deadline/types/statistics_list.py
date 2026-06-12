"""Generated from Smithy shape ``com.amazonaws.deadline#StatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.statistics

StatisticsList: TypeAlias = list["aws_sdk_deadline.types.statistics.Statistics"]


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsList) -> list:
    import aws_sdk_deadline.types.statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatisticsList:
    import aws_sdk_deadline.types.statistics

    out: StatisticsList = []
    for item in data:
        out.append(aws_sdk_deadline.types.statistics.deserialize_json(item))
    return out
