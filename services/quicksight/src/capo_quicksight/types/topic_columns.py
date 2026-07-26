"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_column

TopicColumns: TypeAlias = list["capo_quicksight.types.topic_column.TopicColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicColumns) -> list:
    import capo_quicksight.types.topic_column

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicColumns:
    import capo_quicksight.types.topic_column

    out: TopicColumns = []
    for item in data:
        out.append(capo_quicksight.types.topic_column.deserialize_json(item))
    return out
