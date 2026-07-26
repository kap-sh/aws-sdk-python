"""Generated from Smithy shape ``com.amazonaws.qbusiness#TopicConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.topic_configuration

TopicConfigurations: TypeAlias = list[
    "capo_qbusiness.types.topic_configuration.TopicConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicConfigurations) -> list:
    import capo_qbusiness.types.topic_configuration

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.topic_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicConfigurations:
    import capo_qbusiness.types.topic_configuration

    out: TopicConfigurations = []
    for item in data:
        out.append(capo_qbusiness.types.topic_configuration.deserialize_json(item))
    return out
