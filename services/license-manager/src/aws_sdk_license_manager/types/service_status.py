"""Generated from Smithy shape ``com.amazonaws.licensemanager#ServiceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.cross_account_discovery_service_status
    import aws_sdk_license_manager.types.cross_region_discovery_status


class ServiceStatus(TypedDict, closed=True):
    cross_account_discovery: NotRequired[
        "aws_sdk_license_manager.types.cross_account_discovery_service_status.CrossAccountDiscoveryServiceStatus"
    ]
    """<p>Status of cross-account discovery service.</p>"""
    cross_region_discovery: NotRequired[
        "aws_sdk_license_manager.types.cross_region_discovery_status.CrossRegionDiscoveryStatus"
    ]
    """<p>Status of cross-region discovery service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceStatus) -> dict:
    out: dict = {}
    if "cross_account_discovery" in value:
        import aws_sdk_license_manager.types.cross_account_discovery_service_status

        out["CrossAccountDiscovery"] = (
            aws_sdk_license_manager.types.cross_account_discovery_service_status.serialize_aws_json_1_1(
                value["cross_account_discovery"]
            )
        )
    if "cross_region_discovery" in value:
        import aws_sdk_license_manager.types.cross_region_discovery_status

        out["CrossRegionDiscovery"] = (
            aws_sdk_license_manager.types.cross_region_discovery_status.serialize_aws_json_1_1(
                value["cross_region_discovery"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceStatus:
    out: ServiceStatus = {}  # type: ignore[typeddict-item]
    if "CrossAccountDiscovery" in data:
        import aws_sdk_license_manager.types.cross_account_discovery_service_status

        out["cross_account_discovery"] = (
            aws_sdk_license_manager.types.cross_account_discovery_service_status.deserialize_aws_json_1_1(
                data["CrossAccountDiscovery"]
            )
        )
    if "CrossRegionDiscovery" in data:
        import aws_sdk_license_manager.types.cross_region_discovery_status

        out["cross_region_discovery"] = (
            aws_sdk_license_manager.types.cross_region_discovery_status.deserialize_aws_json_1_1(
                data["CrossRegionDiscovery"]
            )
        )
    return out
