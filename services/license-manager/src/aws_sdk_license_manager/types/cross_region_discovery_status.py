"""Generated from Smithy shape ``com.amazonaws.licensemanager#CrossRegionDiscoveryStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.region_status_map


class CrossRegionDiscoveryStatus(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_license_manager.types.region_status_map.RegionStatusMap"
    ]
    """<p>Map of region status messages for cross-region discovery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossRegionDiscoveryStatus) -> dict:
    out: dict = {}
    if "message" in value:
        import aws_sdk_license_manager.types.region_status_map

        out["Message"] = (
            aws_sdk_license_manager.types.region_status_map.serialize_aws_json_1_1(
                value["message"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CrossRegionDiscoveryStatus:
    out: CrossRegionDiscoveryStatus = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        import aws_sdk_license_manager.types.region_status_map

        out["message"] = (
            aws_sdk_license_manager.types.region_status_map.deserialize_aws_json_1_1(
                data["Message"]
            )
        )
    return out
