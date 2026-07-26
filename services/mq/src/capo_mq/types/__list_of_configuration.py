"""Generated from Smithy shape ``com.amazonaws.mq#__listOfConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.configuration

__listOfConfiguration: TypeAlias = list["capo_mq.types.configuration.Configuration"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConfiguration) -> list:
    import capo_mq.types.configuration

    out: list = []
    for item in value:
        out.append(capo_mq.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConfiguration:
    import capo_mq.types.configuration

    out: __listOfConfiguration = []
    for item in data:
        out.append(capo_mq.types.configuration.deserialize_json(item))
    return out
