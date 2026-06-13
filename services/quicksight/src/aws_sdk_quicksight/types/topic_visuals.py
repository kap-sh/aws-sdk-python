"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicVisuals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_visual

TopicVisuals: TypeAlias = list["aws_sdk_quicksight.types.topic_visual.TopicVisual"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicVisuals) -> list:
    import aws_sdk_quicksight.types.topic_visual

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_visual.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicVisuals:
    import aws_sdk_quicksight.types.topic_visual

    out: TopicVisuals = []
    for item in data:
        out.append(aws_sdk_quicksight.types.topic_visual.deserialize_json(item))
    return out
