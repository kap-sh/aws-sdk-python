"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEc2InstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.ip_v4_address_list
    import capo_inspector2.types.ip_v6_address_list
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.platform


class AwsEc2InstanceDetails(TypedDict, closed=True):
    type: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The type of the Amazon EC2 instance.</p>"""
    image_id: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The image ID of the Amazon EC2 instance.</p>"""
    ip_v4_addresses: NotRequired[
        "capo_inspector2.types.ip_v4_address_list.IpV4AddressList"
    ]
    """<p>The IPv4 addresses of the Amazon EC2 instance.</p>"""
    ip_v6_addresses: NotRequired[
        "capo_inspector2.types.ip_v6_address_list.IpV6AddressList"
    ]
    """<p>The IPv6 addresses of the Amazon EC2 instance.</p>"""
    key_name: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The name of the key pair used to launch the Amazon EC2 instance.</p>"""
    iam_instance_profile_arn: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IAM instance profile ARN of the Amazon EC2 instance.</p>"""
    vpc_id: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The VPC ID of the Amazon EC2 instance.</p>"""
    subnet_id: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The subnet ID of the Amazon EC2 instance.</p>"""
    launched_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the Amazon EC2 instance was launched at.</p>"""
    platform: NotRequired["capo_inspector2.types.platform.Platform"]
    """<p>The platform of the Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "ip_v4_addresses" in value:
        import capo_inspector2.types.ip_v4_address_list

        out["ipV4Addresses"] = capo_inspector2.types.ip_v4_address_list.serialize_json(
            value["ip_v4_addresses"]
        )
    if "ip_v6_addresses" in value:
        import capo_inspector2.types.ip_v6_address_list

        out["ipV6Addresses"] = capo_inspector2.types.ip_v6_address_list.serialize_json(
            value["ip_v6_addresses"]
        )
    if "key_name" in value:
        out["keyName"] = value["key_name"]
    if "iam_instance_profile_arn" in value:
        out["iamInstanceProfileArn"] = value["iam_instance_profile_arn"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "launched_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["launchedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["launched_at"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> AwsEc2InstanceDetails:
    out: AwsEc2InstanceDetails = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "imageId" in data:
        out["image_id"] = data["imageId"]
    if "ipV4Addresses" in data:
        import capo_inspector2.types.ip_v4_address_list

        out["ip_v4_addresses"] = (
            capo_inspector2.types.ip_v4_address_list.deserialize_json(
                data["ipV4Addresses"]
            )
        )
    if "ipV6Addresses" in data:
        import capo_inspector2.types.ip_v6_address_list

        out["ip_v6_addresses"] = (
            capo_inspector2.types.ip_v6_address_list.deserialize_json(
                data["ipV6Addresses"]
            )
        )
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    if "iamInstanceProfileArn" in data:
        out["iam_instance_profile_arn"] = data["iamInstanceProfileArn"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "launchedAt" in data:
        import capo_inspector2.types.date_time_timestamp

        out["launched_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["launchedAt"]
        )
    if "platform" in data:
        out["platform"] = data["platform"]
    return out
