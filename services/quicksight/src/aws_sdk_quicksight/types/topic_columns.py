"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_column

TopicColumns: TypeAlias = list["aws_sdk_quicksight.types.topic_column.TopicColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicColumns) -> list:
    import aws_sdk_quicksight.types.topic_column

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicColumns:
    import aws_sdk_quicksight.types.topic_column

    out: TopicColumns = []
    for item in data:
        out.append(aws_sdk_quicksight.types.topic_column.deserialize_json(item))
    return out
