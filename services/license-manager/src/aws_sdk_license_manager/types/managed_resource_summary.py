"""Generated from Smithy shape ``com.amazonaws.licensemanager#ManagedResourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_long
    import aws_sdk_license_manager.types.resource_type


class ManagedResourceSummary(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_license_manager.types.resource_type.ResourceType"
    ]
    """<p>Type of resource associated with a license.</p>"""
    association_count: NotRequired["aws_sdk_license_manager.types.box_long.BoxLong"]
    """<p>Number of resources associated with licenses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedResourceSummary) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_license_manager.types.resource_type

        out["ResourceType"] = (
            aws_sdk_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "association_count" in value:
        out["AssociationCount"] = value["association_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedResourceSummary:
    out: ManagedResourceSummary = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_license_manager.types.resource_type

        out["resource_type"] = (
            aws_sdk_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "AssociationCount" in data:
        out["association_count"] = data["AssociationCount"]
    return out
