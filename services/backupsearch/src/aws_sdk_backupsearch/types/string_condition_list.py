"""Generated from Smithy shape ``com.amazonaws.backupsearch#StringConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.string_condition

StringConditionList: TypeAlias = list[
    "aws_sdk_backupsearch.types.string_condition.StringCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringConditionList) -> list:
    import aws_sdk_backupsearch.types.string_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_backupsearch.types.string_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> StringConditionList:
    import aws_sdk_backupsearch.types.string_condition

    out: StringConditionList = []
    for item in data:
        out.append(aws_sdk_backupsearch.types.string_condition.deserialize_json(item))
    return out
