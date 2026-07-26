"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotTwinMakerSourceConfigurationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.iot_twin_maker_source_configuration_filter

IotTwinMakerSourceConfigurationFilters: TypeAlias = list[
    "capo_iottwinmaker.types.iot_twin_maker_source_configuration_filter.IotTwinMakerSourceConfigurationFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IotTwinMakerSourceConfigurationFilters) -> list:
    import capo_iottwinmaker.types.iot_twin_maker_source_configuration_filter

    out: list = []
    for item in value:
        out.append(
            capo_iottwinmaker.types.iot_twin_maker_source_configuration_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IotTwinMakerSourceConfigurationFilters:
    import capo_iottwinmaker.types.iot_twin_maker_source_configuration_filter

    out: IotTwinMakerSourceConfigurationFilters = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.iot_twin_maker_source_configuration_filter.deserialize_json(
                item
            )
        )
    return out
