"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotSiteWiseSourceConfigurationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.iot_site_wise_source_configuration_filter

IotSiteWiseSourceConfigurationFilters: TypeAlias = list[
    "capo_iottwinmaker.types.iot_site_wise_source_configuration_filter.IotSiteWiseSourceConfigurationFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseSourceConfigurationFilters) -> list:
    import capo_iottwinmaker.types.iot_site_wise_source_configuration_filter

    out: list = []
    for item in value:
        out.append(
            capo_iottwinmaker.types.iot_site_wise_source_configuration_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IotSiteWiseSourceConfigurationFilters:
    import capo_iottwinmaker.types.iot_site_wise_source_configuration_filter

    out: IotSiteWiseSourceConfigurationFilters = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.iot_site_wise_source_configuration_filter.deserialize_json(
                item
            )
        )
    return out
