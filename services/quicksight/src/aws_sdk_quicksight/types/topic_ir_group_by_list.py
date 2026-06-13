"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_ir_group_by

TopicIRGroupByList: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_ir_group_by.TopicIRGroupBy"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRGroupByList) -> list:
    import aws_sdk_quicksight.types.topic_ir_group_by

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_ir_group_by.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicIRGroupByList:
    import aws_sdk_quicksight.types.topic_ir_group_by

    out: TopicIRGroupByList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.topic_ir_group_by.deserialize_json(item))
    return out
