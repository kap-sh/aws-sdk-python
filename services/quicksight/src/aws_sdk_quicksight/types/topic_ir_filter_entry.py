"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_ir_filter_option

TopicIRFilterEntry: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_ir_filter_option.TopicIRFilterOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRFilterEntry) -> list:
    import aws_sdk_quicksight.types.topic_ir_filter_option

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_ir_filter_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicIRFilterEntry:
    import aws_sdk_quicksight.types.topic_ir_filter_option

    out: TopicIRFilterEntry = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.topic_ir_filter_option.deserialize_json(item)
        )
    return out
