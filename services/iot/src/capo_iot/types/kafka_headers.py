"""Generated from Smithy shape ``com.amazonaws.iot#KafkaHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.kafka_action_header

KafkaHeaders: TypeAlias = list["capo_iot.types.kafka_action_header.KafkaActionHeader"]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaHeaders) -> list:
    import capo_iot.types.kafka_action_header

    out: list = []
    for item in value:
        out.append(capo_iot.types.kafka_action_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> KafkaHeaders:
    import capo_iot.types.kafka_action_header

    out: KafkaHeaders = []
    for item in data:
        out.append(capo_iot.types.kafka_action_header.deserialize_json(item))
    return out
