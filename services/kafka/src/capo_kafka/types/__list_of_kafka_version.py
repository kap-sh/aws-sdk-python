"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfKafkaVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.kafka_version

__listOfKafkaVersion: TypeAlias = list["capo_kafka.types.kafka_version.KafkaVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKafkaVersion) -> list:
    import capo_kafka.types.kafka_version

    out: list = []
    for item in value:
        out.append(capo_kafka.types.kafka_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKafkaVersion:
    import capo_kafka.types.kafka_version

    out: __listOfKafkaVersion = []
    for item in data:
        out.append(capo_kafka.types.kafka_version.deserialize_json(item))
    return out
