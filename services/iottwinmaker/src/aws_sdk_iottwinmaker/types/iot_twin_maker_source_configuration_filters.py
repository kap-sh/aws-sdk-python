"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotTwinMakerSourceConfigurationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filter

IotTwinMakerSourceConfigurationFilters: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filter.IotTwinMakerSourceConfigurationFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IotTwinMakerSourceConfigurationFilters) -> list:
    import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IotTwinMakerSourceConfigurationFilters:
    import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filter

    out: IotTwinMakerSourceConfigurationFilters = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration_filter.deserialize_json(
                item
            )
        )
    return out
