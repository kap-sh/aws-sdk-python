"""Generated from Smithy shape ``com.amazonaws.qbusiness#TopicConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.topic_configuration

TopicConfigurations: TypeAlias = list[
    "aws_sdk_qbusiness.types.topic_configuration.TopicConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicConfigurations) -> list:
    import aws_sdk_qbusiness.types.topic_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.topic_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicConfigurations:
    import aws_sdk_qbusiness.types.topic_configuration

    out: TopicConfigurations = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.topic_configuration.deserialize_json(item))
    return out
