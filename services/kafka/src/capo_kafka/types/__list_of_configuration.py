"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.configuration

__listOfConfiguration: TypeAlias = list["capo_kafka.types.configuration.Configuration"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConfiguration) -> list:
    import capo_kafka.types.configuration

    out: list = []
    for item in value:
        out.append(capo_kafka.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConfiguration:
    import capo_kafka.types.configuration

    out: __listOfConfiguration = []
    for item in data:
        out.append(capo_kafka.types.configuration.deserialize_json(item))
    return out
