"""Generated from Smithy shape ``com.amazonaws.kendra#SiteMapsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.site_maps_list


class SiteMapsConfiguration(TypedDict):
    site_maps: "aws_sdk_kendra.types.site_maps_list.SiteMapsList"
    """<p>The list of sitemap URLs of the websites you want to crawl.</p> <p>The list can include a maximum of three sitemap URLs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SiteMapsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.site_maps_list

    out["SiteMaps"] = aws_sdk_kendra.types.site_maps_list.serialize_aws_json_1_1(
        value["site_maps"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SiteMapsConfiguration:
    out: SiteMapsConfiguration = {}  # type: ignore[typeddict-item]
    if "SiteMaps" in data:
        import aws_sdk_kendra.types.site_maps_list

        out["site_maps"] = aws_sdk_kendra.types.site_maps_list.deserialize_aws_json_1_1(
            data["SiteMaps"]
        )
    else:
        raise DeserializationError("SiteMapsConfiguration.site_maps required")
    return out
