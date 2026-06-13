"""Generated from Smithy shape ``com.amazonaws.backupsearch#LongConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.long_condition

LongConditionList: TypeAlias = list[
    "aws_sdk_backupsearch.types.long_condition.LongCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: LongConditionList) -> list:
    import aws_sdk_backupsearch.types.long_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_backupsearch.types.long_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> LongConditionList:
    import aws_sdk_backupsearch.types.long_condition

    out: LongConditionList = []
    for item in data:
        out.append(aws_sdk_backupsearch.types.long_condition.deserialize_json(item))
    return out
