"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_long
    import aws_sdk_license_manager.types.date_time
    import aws_sdk_license_manager.types.resource_type
    import aws_sdk_license_manager.types.string


class LicenseConfigurationUsage(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_license_manager.types.resource_type.ResourceType"
    ]
    """<p>Type of resource.</p>"""
    resource_status: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Status of the resource.</p>"""
    resource_owner_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>ID of the account that owns the resource.</p>"""
    association_time: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>Time when the license configuration was initially associated with the resource.</p>"""
    consumed_licenses: NotRequired["aws_sdk_license_manager.types.box_long.BoxLong"]
    """<p>Number of licenses consumed by the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationUsage) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        import aws_sdk_license_manager.types.resource_type

        out["ResourceType"] = (
            aws_sdk_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "resource_status" in value:
        out["ResourceStatus"] = value["resource_status"]
    if "resource_owner_id" in value:
        out["ResourceOwnerId"] = value["resource_owner_id"]
    if "association_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["AssociationTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
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
        import aws_sdk_license_manager.types.resource_type

        out["resource_type"] = (
            aws_sdk_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ResourceStatus" in data:
        out["resource_status"] = data["ResourceStatus"]
    if "ResourceOwnerId" in data:
        out["resource_owner_id"] = data["ResourceOwnerId"]
    if "AssociationTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["association_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["AssociationTime"]
            )
        )
    if "ConsumedLicenses" in data:
        out["consumed_licenses"] = data["ConsumedLicenses"]
    return out
