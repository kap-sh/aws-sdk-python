"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.position_configuration_item

PositionConfigurationList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.position_configuration_item.PositionConfigurationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: PositionConfigurationList) -> list:
    import aws_sdk_iot_wireless.types.position_configuration_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.position_configuration_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PositionConfigurationList:
    import aws_sdk_iot_wireless.types.position_configuration_item

    out: PositionConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.position_configuration_item.deserialize_json(
                item
            )
        )
    return out
