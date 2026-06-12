"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotSiteWiseSourceConfigurationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filter

IotSiteWiseSourceConfigurationFilters: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filter.IotSiteWiseSourceConfigurationFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseSourceConfigurationFilters) -> list:
    import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IotSiteWiseSourceConfigurationFilters:
    import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filter

    out: IotSiteWiseSourceConfigurationFilters = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filter.deserialize_json(
                item
            )
        )
    return out
