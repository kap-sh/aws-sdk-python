"""Generated from Smithy shape ``com.amazonaws.iot#KafkaHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.kafka_action_header

KafkaHeaders: TypeAlias = list[
    "aws_sdk_iot.types.kafka_action_header.KafkaActionHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaHeaders) -> list:
    import aws_sdk_iot.types.kafka_action_header

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.kafka_action_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> KafkaHeaders:
    import aws_sdk_iot.types.kafka_action_header

    out: KafkaHeaders = []
    for item in data:
        out.append(aws_sdk_iot.types.kafka_action_header.deserialize_json(item))
    return out
