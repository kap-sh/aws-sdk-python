"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeGatewayInformationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cloud_watch_log_group_arn
    import aws_sdk_storage_gateway.types.deprecation_date
    import aws_sdk_storage_gateway.types.ec2_instance_id
    import aws_sdk_storage_gateway.types.ec2_instance_region
    import aws_sdk_storage_gateway.types.endpoint_type
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.gateway_capacity
    import aws_sdk_storage_gateway.types.gateway_id
    import aws_sdk_storage_gateway.types.gateway_network_interfaces
    import aws_sdk_storage_gateway.types.gateway_state
    import aws_sdk_storage_gateway.types.gateway_timezone
    import aws_sdk_storage_gateway.types.gateway_type
    import aws_sdk_storage_gateway.types.host_environment
    import aws_sdk_storage_gateway.types.host_environment_id
    import aws_sdk_storage_gateway.types.last_software_update
    import aws_sdk_storage_gateway.types.next_update_availability_date
    import aws_sdk_storage_gateway.types.software_updates_end_date
    import aws_sdk_storage_gateway.types.software_version
    import aws_sdk_storage_gateway.types.string
    import aws_sdk_storage_gateway.types.supported_gateway_capacities
    import aws_sdk_storage_gateway.types.tags


class DescribeGatewayInformationOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    gateway_id: NotRequired["aws_sdk_storage_gateway.types.gateway_id.GatewayId"]
    """<p>The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.</p>"""
    gateway_name: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>The name you configured for your gateway.</p>"""
    gateway_timezone: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_timezone.GatewayTimezone"
    ]
    """<p>A value that indicates the time zone configured for the gateway.</p>"""
    gateway_state: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_state.GatewayState"
    ]
    """<p>A value that indicates the operating state of the gateway.</p>"""
    gateway_network_interfaces: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_network_interfaces.GatewayNetworkInterfaces"
    ]
    """<p>A <a>NetworkInterface</a> array that contains descriptions of the gateway network interfaces.</p>"""
    gateway_type: NotRequired["aws_sdk_storage_gateway.types.gateway_type.GatewayType"]
    """<p>The type of the gateway.</p> <important> <p>Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit <a href=\"https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/\">this blog post</a>.</p> </important>"""
    next_update_availability_date: NotRequired[
        "aws_sdk_storage_gateway.types.next_update_availability_date.NextUpdateAvailabilityDate"
    ]
    """<p>The date on which an update to the gateway is available. This date is in the time zone of the gateway. If the gateway is not available for an update this field is not returned in the response.</p>"""
    last_software_update: NotRequired[
        "aws_sdk_storage_gateway.types.last_software_update.LastSoftwareUpdate"
    ]
    """<p>The date on which the last software update was applied to the gateway. If the gateway has never been updated, this field does not return a value in the response. This only only exist and returns once it have been chosen and set by the SGW service, based on the OS version of the gateway VM</p>"""
    ec2_instance_id: NotRequired[
        "aws_sdk_storage_gateway.types.ec2_instance_id.Ec2InstanceId"
    ]
    """<p>The ID of the Amazon EC2 instance that was used to launch the gateway.</p>"""
    ec2_instance_region: NotRequired[
        "aws_sdk_storage_gateway.types.ec2_instance_region.Ec2InstanceRegion"
    ]
    """<p>The Amazon Web Services Region where the Amazon EC2 instance is located.</p>"""
    tags: NotRequired["aws_sdk_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags assigned to the gateway, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the <code>ListTagsForResource</code> API operation.</p>"""
    vpc_endpoint: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>The configuration settings for the virtual private cloud (VPC) endpoint for your gateway.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_storage_gateway.types.cloud_watch_log_group_arn.CloudWatchLogGroupARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that is used to monitor events in the gateway. This field only only exist and returns once it have been chosen and set by the SGW service, based on the OS version of the gateway VM</p>"""
    host_environment: NotRequired[
        "aws_sdk_storage_gateway.types.host_environment.HostEnvironment"
    ]
    """<p>The type of hardware or software platform on which the gateway is running.</p> <note> <p>Tape Gateway is no longer available on Snow Family devices.</p> </note>"""
    endpoint_type: NotRequired[
        "aws_sdk_storage_gateway.types.endpoint_type.EndpointType"
    ]
    """<p>The type of endpoint for your gateway.</p> <p>Valid Values: <code>STANDARD</code> | <code>FIPS</code> </p>"""
    software_updates_end_date: NotRequired[
        "aws_sdk_storage_gateway.types.software_updates_end_date.SoftwareUpdatesEndDate"
    ]
    """<p>Date after which this gateway will not receive software updates for new features.</p>"""
    deprecation_date: NotRequired[
        "aws_sdk_storage_gateway.types.deprecation_date.DeprecationDate"
    ]
    """<p>Date after which this gateway will not receive software updates for new features and bug fixes.</p>"""
    gateway_capacity: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_capacity.GatewayCapacity"
    ]
    """<p>Specifies the size of the gateway's metadata cache.</p>"""
    supported_gateway_capacities: NotRequired[
        "aws_sdk_storage_gateway.types.supported_gateway_capacities.SupportedGatewayCapacities"
    ]
    """<p>A list of the metadata cache sizes that the gateway can support based on its current hardware specifications.</p>"""
    host_environment_id: NotRequired[
        "aws_sdk_storage_gateway.types.host_environment_id.HostEnvironmentId"
    ]
    """<p>A unique identifier for the specific instance of the host platform running the gateway. This value is only available for certain host environments, and its format depends on the host environment type.</p>"""
    software_version: NotRequired[
        "aws_sdk_storage_gateway.types.software_version.SoftwareVersion"
    ]
    """<p>The version number of the software running on the gateway appliance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayInformationOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "gateway_name" in value:
        out["GatewayName"] = value["gateway_name"]
    if "gateway_timezone" in value:
        out["GatewayTimezone"] = value["gateway_timezone"]
    if "gateway_state" in value:
        out["GatewayState"] = value["gateway_state"]
    if "gateway_network_interfaces" in value:
        import aws_sdk_storage_gateway.types.gateway_network_interfaces

        out["GatewayNetworkInterfaces"] = (
            aws_sdk_storage_gateway.types.gateway_network_interfaces.serialize_aws_json_1_1(
                value["gateway_network_interfaces"]
            )
        )
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "next_update_availability_date" in value:
        out["NextUpdateAvailabilityDate"] = value["next_update_availability_date"]
    if "last_software_update" in value:
        out["LastSoftwareUpdate"] = value["last_software_update"]
    if "ec2_instance_id" in value:
        out["Ec2InstanceId"] = value["ec2_instance_id"]
    if "ec2_instance_region" in value:
        out["Ec2InstanceRegion"] = value["ec2_instance_region"]
    if "tags" in value:
        import aws_sdk_storage_gateway.types.tags

        out["Tags"] = aws_sdk_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_endpoint" in value:
        out["VPCEndpoint"] = value["vpc_endpoint"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupARN"] = value["cloud_watch_log_group_arn"]
    if "host_environment" in value:
        import aws_sdk_storage_gateway.types.host_environment

        out["HostEnvironment"] = (
            aws_sdk_storage_gateway.types.host_environment.serialize_aws_json_1_1(
                value["host_environment"]
            )
        )
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "software_updates_end_date" in value:
        out["SoftwareUpdatesEndDate"] = value["software_updates_end_date"]
    if "deprecation_date" in value:
        out["DeprecationDate"] = value["deprecation_date"]
    if "gateway_capacity" in value:
        import aws_sdk_storage_gateway.types.gateway_capacity

        out["GatewayCapacity"] = (
            aws_sdk_storage_gateway.types.gateway_capacity.serialize_aws_json_1_1(
                value["gateway_capacity"]
            )
        )
    if "supported_gateway_capacities" in value:
        import aws_sdk_storage_gateway.types.supported_gateway_capacities

        out["SupportedGatewayCapacities"] = (
            aws_sdk_storage_gateway.types.supported_gateway_capacities.serialize_aws_json_1_1(
                value["supported_gateway_capacities"]
            )
        )
    if "host_environment_id" in value:
        out["HostEnvironmentId"] = value["host_environment_id"]
    if "software_version" in value:
        out["SoftwareVersion"] = value["software_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayInformationOutput:
    out: DescribeGatewayInformationOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    if "GatewayName" in data:
        out["gateway_name"] = data["GatewayName"]
    if "GatewayTimezone" in data:
        out["gateway_timezone"] = data["GatewayTimezone"]
    if "GatewayState" in data:
        out["gateway_state"] = data["GatewayState"]
    if "GatewayNetworkInterfaces" in data:
        import aws_sdk_storage_gateway.types.gateway_network_interfaces

        out["gateway_network_interfaces"] = (
            aws_sdk_storage_gateway.types.gateway_network_interfaces.deserialize_aws_json_1_1(
                data["GatewayNetworkInterfaces"]
            )
        )
    if "GatewayType" in data:
        out["gateway_type"] = data["GatewayType"]
    if "NextUpdateAvailabilityDate" in data:
        out["next_update_availability_date"] = data["NextUpdateAvailabilityDate"]
    if "LastSoftwareUpdate" in data:
        out["last_software_update"] = data["LastSoftwareUpdate"]
    if "Ec2InstanceId" in data:
        out["ec2_instance_id"] = data["Ec2InstanceId"]
    if "Ec2InstanceRegion" in data:
        out["ec2_instance_region"] = data["Ec2InstanceRegion"]
    if "Tags" in data:
        import aws_sdk_storage_gateway.types.tags

        out["tags"] = aws_sdk_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "VPCEndpoint" in data:
        out["vpc_endpoint"] = data["VPCEndpoint"]
    if "CloudWatchLogGroupARN" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupARN"]
    if "HostEnvironment" in data:
        import aws_sdk_storage_gateway.types.host_environment

        out["host_environment"] = (
            aws_sdk_storage_gateway.types.host_environment.deserialize_aws_json_1_1(
                data["HostEnvironment"]
            )
        )
    if "EndpointType" in data:
        out["endpoint_type"] = data["EndpointType"]
    if "SoftwareUpdatesEndDate" in data:
        out["software_updates_end_date"] = data["SoftwareUpdatesEndDate"]
    if "DeprecationDate" in data:
        out["deprecation_date"] = data["DeprecationDate"]
    if "GatewayCapacity" in data:
        import aws_sdk_storage_gateway.types.gateway_capacity

        out["gateway_capacity"] = (
            aws_sdk_storage_gateway.types.gateway_capacity.deserialize_aws_json_1_1(
                data["GatewayCapacity"]
            )
        )
    if "SupportedGatewayCapacities" in data:
        import aws_sdk_storage_gateway.types.supported_gateway_capacities

        out["supported_gateway_capacities"] = (
            aws_sdk_storage_gateway.types.supported_gateway_capacities.deserialize_aws_json_1_1(
                data["SupportedGatewayCapacities"]
            )
        )
    if "HostEnvironmentId" in data:
        out["host_environment_id"] = data["HostEnvironmentId"]
    if "SoftwareVersion" in data:
        out["software_version"] = data["SoftwareVersion"]
    return out
