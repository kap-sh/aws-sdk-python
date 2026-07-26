"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#SnsTopics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.sns_topic

SnsTopics: TypeAlias = list["capo_elastic_transcoder.types.sns_topic.SnsTopic"]


# --- restJson1 ser/de ---
def serialize_json(value: SnsTopics) -> list:
    return list(value)


def deserialize_json(data: list) -> SnsTopics:
    return list(data)
