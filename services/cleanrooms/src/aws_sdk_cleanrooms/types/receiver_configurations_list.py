"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ReceiverConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.receiver_configuration

ReceiverConfigurationsList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.receiver_configuration.ReceiverConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReceiverConfigurationsList) -> list:
    import aws_sdk_cleanrooms.types.receiver_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.receiver_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReceiverConfigurationsList:
    import aws_sdk_cleanrooms.types.receiver_configuration

    out: ReceiverConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.receiver_configuration.deserialize_json(item)
        )
    return out
