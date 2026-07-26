"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfCompatibleKafkaVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.compatible_kafka_version

__listOfCompatibleKafkaVersion: TypeAlias = list[
    "capo_kafka.types.compatible_kafka_version.CompatibleKafkaVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCompatibleKafkaVersion) -> list:
    import capo_kafka.types.compatible_kafka_version

    out: list = []
    for item in value:
        out.append(capo_kafka.types.compatible_kafka_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCompatibleKafkaVersion:
    import capo_kafka.types.compatible_kafka_version

    out: __listOfCompatibleKafkaVersion = []
    for item in data:
        out.append(capo_kafka.types.compatible_kafka_version.deserialize_json(item))
    return out
