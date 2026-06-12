"""Generated from Smithy shape ``com.amazonaws.licensemanager#ResourceInventory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.resource_type
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.string_list


class ResourceInventory(TypedDict):
    resource_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_license_manager.types.resource_type.ResourceType"
    ]
    """<p>Type of resource.</p>"""
    resource_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    platform: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Platform of the resource.</p>"""
    platform_version: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Platform version of the resource in the inventory.</p>"""
    resource_owning_account_id: NotRequired[
        "aws_sdk_license_manager.types.string.String"
    ]
    """<p>ID of the account that owns the resource.</p>"""
    marketplace_product_codes: NotRequired[
        "aws_sdk_license_manager.types.string_list.StringList"
    ]
    """<p>List of Marketplace product codes associated with the resource.</p>"""
    usage_operation: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Usage operation value that corresponds to the license type for billing purposes.</p>"""
    ami_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Machine Image (AMI) ID associated with the resource.</p>"""
    host_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Dedicated Host ID where the resource is running.</p>"""
    region: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Region where the resource is located.</p>"""
    instance_type: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>EC2 instance type of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInventory) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_license_manager.types.resource_type

        out["ResourceType"] = (
            aws_sdk_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "resource_owning_account_id" in value:
        out["ResourceOwningAccountId"] = value["resource_owning_account_id"]
    if "marketplace_product_codes" in value:
        import aws_sdk_license_manager.types.string_list

        out["MarketplaceProductCodes"] = (
            aws_sdk_license_manager.types.string_list.serialize_aws_json_1_1(
                value["marketplace_product_codes"]
            )
        )
    if "usage_operation" in value:
        out["UsageOperation"] = value["usage_operation"]
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "host_id" in value:
        out["HostId"] = value["host_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceInventory:
    out: ResourceInventory = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        import aws_sdk_license_manager.types.resource_type

        out["resource_type"] = (
            aws_sdk_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "ResourceOwningAccountId" in data:
        out["resource_owning_account_id"] = data["ResourceOwningAccountId"]
    if "MarketplaceProductCodes" in data:
        import aws_sdk_license_manager.types.string_list

        out["marketplace_product_codes"] = (
            aws_sdk_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["MarketplaceProductCodes"]
            )
        )
    if "UsageOperation" in data:
        out["usage_operation"] = data["UsageOperation"]
    if "AmiId" in data:
        out["ami_id"] = data["AmiId"]
    if "HostId" in data:
        out["host_id"] = data["HostId"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    return out
