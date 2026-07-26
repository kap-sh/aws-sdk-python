"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ReceiverConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.receiver_configuration

ReceiverConfigurationsList: TypeAlias = list[
    "capo_cleanrooms.types.receiver_configuration.ReceiverConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReceiverConfigurationsList) -> list:
    import capo_cleanrooms.types.receiver_configuration

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.receiver_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReceiverConfigurationsList:
    import capo_cleanrooms.types.receiver_configuration

    out: ReceiverConfigurationsList = []
    for item in data:
        out.append(capo_cleanrooms.types.receiver_configuration.deserialize_json(item))
    return out
