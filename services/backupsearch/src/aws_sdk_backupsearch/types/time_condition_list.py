"""Generated from Smithy shape ``com.amazonaws.backupsearch#TimeConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.time_condition

TimeConditionList: TypeAlias = list[
    "aws_sdk_backupsearch.types.time_condition.TimeCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeConditionList) -> list:
    import aws_sdk_backupsearch.types.time_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_backupsearch.types.time_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeConditionList:
    import aws_sdk_backupsearch.types.time_condition

    out: TimeConditionList = []
    for item in data:
        out.append(aws_sdk_backupsearch.types.time_condition.deserialize_json(item))
    return out
