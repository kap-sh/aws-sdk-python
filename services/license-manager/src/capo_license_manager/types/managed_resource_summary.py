"""Generated from Smithy shape ``com.amazonaws.licensemanager#ManagedResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.box_long
    import capo_license_manager.types.resource_type


class ManagedResourceSummary(TypedDict, closed=True):
    resource_type: NotRequired["capo_license_manager.types.resource_type.ResourceType"]
    """<p>Type of resource associated with a license.</p>"""
    association_count: NotRequired["capo_license_manager.types.box_long.BoxLong"]
    """<p>Number of resources associated with licenses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedResourceSummary) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_license_manager.types.resource_type

        out["ResourceType"] = (
            capo_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "association_count" in value:
        out["AssociationCount"] = value["association_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedResourceSummary:
    out: ManagedResourceSummary = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_license_manager.types.resource_type

        out["resource_type"] = (
            capo_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "AssociationCount" in data:
        out["association_count"] = data["AssociationCount"]
    return out
