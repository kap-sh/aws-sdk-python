"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_instance_metadata_options
    import aws_sdk_securityhub.types.aws_ec2_instance_monitoring_details
    import aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_list
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsEc2InstanceDetails(TypedDict):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The instance type of the instance. </p>"""
    image_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Machine Image (AMI) ID of the instance.</p>"""
    ip_v4_addresses: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The IPv4 addresses associated with the instance.</p>"""
    ip_v6_addresses: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The IPv6 addresses associated with the instance.</p>"""
    key_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The key name associated with the instance.</p>"""
    iam_instance_profile_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IAM profile ARN of the instance.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC that the instance was launched in.</p>"""
    subnet_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the subnet that the instance was launched in.</p>"""
    launched_at: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the instance was launched.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_list.AwsEc2InstanceNetworkInterfacesList"
    ]
    """<p>The identifiers of the network interfaces for the EC2 instance. The details for each network interface are in a corresponding <code>AwsEc2NetworkInterfacesDetails</code> object.</p>"""
    virtualization_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The virtualization type of the Amazon Machine Image (AMI) required to launch the instance. </p>"""
    metadata_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_instance_metadata_options.AwsEc2InstanceMetadataOptions"
    ]
    """<p>Details about the metadata options for the Amazon EC2 instance. </p>"""
    monitoring: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_instance_monitoring_details.AwsEc2InstanceMonitoringDetails"
    ]
    """<p> Describes the type of monitoring that’s turned on for an instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "ip_v4_addresses" in value:
        import aws_sdk_securityhub.types.string_list

        out["IpV4Addresses"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["ip_v4_addresses"]
        )
    if "ip_v6_addresses" in value:
        import aws_sdk_securityhub.types.string_list

        out["IpV6Addresses"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["ip_v6_addresses"]
        )
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "iam_instance_profile_arn" in value:
        out["IamInstanceProfileArn"] = value["iam_instance_profile_arn"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "launched_at" in value:
        out["LaunchedAt"] = value["launched_at"]
    if "network_interfaces" in value:
        import aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_list

        out["NetworkInterfaces"] = (
            aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_list.serialize_json(
                value["network_interfaces"]
            )
        )
    if "virtualization_type" in value:
        out["VirtualizationType"] = value["virtualization_type"]
    if "metadata_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_instance_metadata_options

        out["MetadataOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_instance_metadata_options.serialize_json(
                value["metadata_options"]
            )
        )
    if "monitoring" in value:
        import aws_sdk_securityhub.types.aws_ec2_instance_monitoring_details

        out["Monitoring"] = (
            aws_sdk_securityhub.types.aws_ec2_instance_monitoring_details.serialize_json(
                value["monitoring"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2InstanceDetails:
    out: AwsEc2InstanceDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "IpV4Addresses" in data:
        import aws_sdk_securityhub.types.string_list

        out["ip_v4_addresses"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["IpV4Addresses"]
        )
    if "IpV6Addresses" in data:
        import aws_sdk_securityhub.types.string_list

        out["ip_v6_addresses"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["IpV6Addresses"]
        )
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "IamInstanceProfileArn" in data:
        out["iam_instance_profile_arn"] = data["IamInstanceProfileArn"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "LaunchedAt" in data:
        out["launched_at"] = data["LaunchedAt"]
    if "NetworkInterfaces" in data:
        import aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_list

        out["network_interfaces"] = (
            aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_list.deserialize_json(
                data["NetworkInterfaces"]
            )
        )
    if "VirtualizationType" in data:
        out["virtualization_type"] = data["VirtualizationType"]
    if "MetadataOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_instance_metadata_options

        out["metadata_options"] = (
            aws_sdk_securityhub.types.aws_ec2_instance_metadata_options.deserialize_json(
                data["MetadataOptions"]
            )
        )
    if "Monitoring" in data:
        import aws_sdk_securityhub.types.aws_ec2_instance_monitoring_details

        out["monitoring"] = (
            aws_sdk_securityhub.types.aws_ec2_instance_monitoring_details.deserialize_json(
                data["Monitoring"]
            )
        )
    return out
