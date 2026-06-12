"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedEc2FleetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.persistent_volume_configuration
    import aws_sdk_deadline.types.service_managed_ec2_auto_scaling_configuration
    import aws_sdk_deadline.types.service_managed_ec2_instance_capabilities
    import aws_sdk_deadline.types.service_managed_ec2_instance_market_options
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.vpc_configuration


class ServiceManagedEc2FleetConfiguration(TypedDict):
    instance_capabilities: "aws_sdk_deadline.types.service_managed_ec2_instance_capabilities.ServiceManagedEc2InstanceCapabilities"
    """<p>The instance capabilities for the service managed EC2 fleet.</p>"""
    instance_market_options: "aws_sdk_deadline.types.service_managed_ec2_instance_market_options.ServiceManagedEc2InstanceMarketOptions"
    """<p>The instance market options for the service managed EC2 fleet.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_deadline.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration for the service managed EC2 fleet.</p>"""
    storage_profile_id: NotRequired[
        "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """<p>The storage profile ID for the service managed EC2 fleet.</p>"""
    persistent_volume_configuration: NotRequired[
        "aws_sdk_deadline.types.persistent_volume_configuration.PersistentVolumeConfiguration"
    ]
    """<p>The persistent volume configuration for the service managed EC2 fleet.</p>"""
    auto_scaling_configuration: NotRequired[
        "aws_sdk_deadline.types.service_managed_ec2_auto_scaling_configuration.ServiceManagedEc2AutoScalingConfiguration"
    ]
    """<p>The auto scaling configuration settings for the service managed EC2 fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedEc2FleetConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.service_managed_ec2_instance_capabilities

    out["instanceCapabilities"] = (
        aws_sdk_deadline.types.service_managed_ec2_instance_capabilities.serialize_json(
            value["instance_capabilities"]
        )
    )
    import aws_sdk_deadline.types.service_managed_ec2_instance_market_options

    out["instanceMarketOptions"] = (
        aws_sdk_deadline.types.service_managed_ec2_instance_market_options.serialize_json(
            value["instance_market_options"]
        )
    )
    if "vpc_configuration" in value:
        import aws_sdk_deadline.types.vpc_configuration

        out["vpcConfiguration"] = (
            aws_sdk_deadline.types.vpc_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "persistent_volume_configuration" in value:
        import aws_sdk_deadline.types.persistent_volume_configuration

        out["persistentVolumeConfiguration"] = (
            aws_sdk_deadline.types.persistent_volume_configuration.serialize_json(
                value["persistent_volume_configuration"]
            )
        )
    if "auto_scaling_configuration" in value:
        import aws_sdk_deadline.types.service_managed_ec2_auto_scaling_configuration

        out["autoScalingConfiguration"] = (
            aws_sdk_deadline.types.service_managed_ec2_auto_scaling_configuration.serialize_json(
                value["auto_scaling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedEc2FleetConfiguration:
    out: ServiceManagedEc2FleetConfiguration = {}  # type: ignore[typeddict-item]
    if "instanceCapabilities" in data:
        import aws_sdk_deadline.types.service_managed_ec2_instance_capabilities

        out["instance_capabilities"] = (
            aws_sdk_deadline.types.service_managed_ec2_instance_capabilities.deserialize_json(
                data["instanceCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2FleetConfiguration.instance_capabilities required"
        )
    if "instanceMarketOptions" in data:
        import aws_sdk_deadline.types.service_managed_ec2_instance_market_options

        out["instance_market_options"] = (
            aws_sdk_deadline.types.service_managed_ec2_instance_market_options.deserialize_json(
                data["instanceMarketOptions"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2FleetConfiguration.instance_market_options required"
        )
    if "vpcConfiguration" in data:
        import aws_sdk_deadline.types.vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_deadline.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    if "persistentVolumeConfiguration" in data:
        import aws_sdk_deadline.types.persistent_volume_configuration

        out["persistent_volume_configuration"] = (
            aws_sdk_deadline.types.persistent_volume_configuration.deserialize_json(
                data["persistentVolumeConfiguration"]
            )
        )
    if "autoScalingConfiguration" in data:
        import aws_sdk_deadline.types.service_managed_ec2_auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            aws_sdk_deadline.types.service_managed_ec2_auto_scaling_configuration.deserialize_json(
                data["autoScalingConfiguration"]
            )
        )
    return out
