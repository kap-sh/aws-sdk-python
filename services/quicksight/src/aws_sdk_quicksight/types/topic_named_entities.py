"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNamedEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_named_entity

TopicNamedEntities: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_named_entity.TopicNamedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicNamedEntities) -> list:
    import aws_sdk_quicksight.types.topic_named_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_named_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicNamedEntities:
    import aws_sdk_quicksight.types.topic_named_entity

    out: TopicNamedEntities = []
    for item in data:
        out.append(aws_sdk_quicksight.types.topic_named_entity.deserialize_json(item))
    return out
