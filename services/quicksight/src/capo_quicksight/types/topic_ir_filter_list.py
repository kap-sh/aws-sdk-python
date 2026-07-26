"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_ir_filter_entry

TopicIRFilterList: TypeAlias = list[
    "capo_quicksight.types.topic_ir_filter_entry.TopicIRFilterEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRFilterList) -> list:
    import capo_quicksight.types.topic_ir_filter_entry

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_ir_filter_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicIRFilterList:
    import capo_quicksight.types.topic_ir_filter_entry

    out: TopicIRFilterList = []
    for item in data:
        out.append(capo_quicksight.types.topic_ir_filter_entry.deserialize_json(item))
    return out
