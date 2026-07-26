"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCalculatedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_calculated_field

TopicCalculatedFields: TypeAlias = list[
    "capo_quicksight.types.topic_calculated_field.TopicCalculatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicCalculatedFields) -> list:
    import capo_quicksight.types.topic_calculated_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_calculated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicCalculatedFields:
    import capo_quicksight.types.topic_calculated_field

    out: TopicCalculatedFields = []
    for item in data:
        out.append(capo_quicksight.types.topic_calculated_field.deserialize_json(item))
    return out
