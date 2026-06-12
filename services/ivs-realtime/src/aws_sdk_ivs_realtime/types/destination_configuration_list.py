"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.destination_configuration

DestinationConfigurationList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.destination_configuration.DestinationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfigurationList) -> list:
    import aws_sdk_ivs_realtime.types.destination_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.destination_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DestinationConfigurationList:
    import aws_sdk_ivs_realtime.types.destination_configuration

    out: DestinationConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.destination_configuration.deserialize_json(item)
        )
    return out
