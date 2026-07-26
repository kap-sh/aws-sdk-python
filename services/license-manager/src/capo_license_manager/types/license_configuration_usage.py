"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.box_long
    import capo_license_manager.types.date_time
    import capo_license_manager.types.resource_type
    import capo_license_manager.types.string


class LicenseConfigurationUsage(TypedDict, closed=True):
    resource_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    resource_type: NotRequired["capo_license_manager.types.resource_type.ResourceType"]
    """<p>Type of resource.</p>"""
    resource_status: NotRequired["capo_license_manager.types.string.String"]
    """<p>Status of the resource.</p>"""
    resource_owner_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>ID of the account that owns the resource.</p>"""
    association_time: NotRequired["capo_license_manager.types.date_time.DateTime"]
    """<p>Time when the license configuration was initially associated with the resource.</p>"""
    consumed_licenses: NotRequired["capo_license_manager.types.box_long.BoxLong"]
    """<p>Number of licenses consumed by the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationUsage) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        import capo_license_manager.types.resource_type

        out["ResourceType"] = (
            capo_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "resource_status" in value:
        out["ResourceStatus"] = value["resource_status"]
    if "resource_owner_id" in value:
        out["ResourceOwnerId"] = value["resource_owner_id"]
    if "association_time" in value:
        import capo_license_manager.types.date_time

        out["AssociationTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["association_time"]
            )
        )
    if "consumed_licenses" in value:
        out["ConsumedLicenses"] = value["consumed_licenses"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseConfigurationUsage:
    out: LicenseConfigurationUsage = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        import capo_license_manager.types.resource_type

        out["resource_type"] = (
            capo_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ResourceStatus" in data:
        out["resource_status"] = data["ResourceStatus"]
    if "ResourceOwnerId" in data:
        out["resource_owner_id"] = data["ResourceOwnerId"]
    if "AssociationTime" in data:
        import capo_license_manager.types.date_time

        out["association_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["AssociationTime"]
            )
        )
    if "ConsumedLicenses" in data:
        out["consumed_licenses"] = data["ConsumedLicenses"]
    return out
