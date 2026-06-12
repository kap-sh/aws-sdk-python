"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionsInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.additional_regions
    import aws_sdk_directory_service.types.region_name


class RegionsInfo(TypedDict):
    primary_region: NotRequired[
        "aws_sdk_directory_service.types.region_name.RegionName"
    ]
    """<p>The Region where the Managed Microsoft AD directory was originally created.</p>"""
    additional_regions: NotRequired[
        "aws_sdk_directory_service.types.additional_regions.AdditionalRegions"
    ]
    """<p>Lists the Regions where the directory has been replicated, excluding the primary Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionsInfo) -> dict:
    out: dict = {}
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    if "additional_regions" in value:
        import aws_sdk_directory_service.types.additional_regions

        out["AdditionalRegions"] = (
            aws_sdk_directory_service.types.additional_regions.serialize_aws_json_1_1(
                value["additional_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionsInfo:
    out: RegionsInfo = {}  # type: ignore[typeddict-item]
    if "PrimaryRegion" in data:
        out["primary_region"] = data["PrimaryRegion"]
    if "AdditionalRegions" in data:
        import aws_sdk_directory_service.types.additional_regions

        out["additional_regions"] = (
            aws_sdk_directory_service.types.additional_regions.deserialize_aws_json_1_1(
                data["AdditionalRegions"]
            )
        )
    return out
