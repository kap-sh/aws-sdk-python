"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCalculatedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_calculated_field

TopicCalculatedFields: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_calculated_field.TopicCalculatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicCalculatedFields) -> list:
    import aws_sdk_quicksight.types.topic_calculated_field

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_calculated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicCalculatedFields:
    import aws_sdk_quicksight.types.topic_calculated_field

    out: TopicCalculatedFields = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.topic_calculated_field.deserialize_json(item)
        )
    return out
