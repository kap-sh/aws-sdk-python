"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_ir_group_by

TopicIRGroupByList: TypeAlias = list[
    "capo_quicksight.types.topic_ir_group_by.TopicIRGroupBy"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRGroupByList) -> list:
    import capo_quicksight.types.topic_ir_group_by

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_ir_group_by.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicIRGroupByList:
    import capo_quicksight.types.topic_ir_group_by

    out: TopicIRGroupByList = []
    for item in data:
        out.append(capo_quicksight.types.topic_ir_group_by.deserialize_json(item))
    return out
