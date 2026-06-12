"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotSiteWiseSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filters


class IotSiteWiseSourceConfiguration(TypedDict):
    filters: NotRequired[
        "aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filters.IotSiteWiseSourceConfigurationFilters"
    ]
    """<p>The AWS IoT SiteWise soucre configuration filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseSourceConfiguration) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filters.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> IotSiteWiseSourceConfiguration:
    out: IotSiteWiseSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
