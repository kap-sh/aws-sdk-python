"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfKafkaVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.kafka_version

__listOfKafkaVersion: TypeAlias = list["aws_sdk_kafka.types.kafka_version.KafkaVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKafkaVersion) -> list:
    import aws_sdk_kafka.types.kafka_version

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.kafka_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKafkaVersion:
    import aws_sdk_kafka.types.kafka_version

    out: __listOfKafkaVersion = []
    for item in data:
        out.append(aws_sdk_kafka.types.kafka_version.deserialize_json(item))
    return out
