"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2Instance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ec2_network_interface_uids
    import aws_sdk_guardduty.types.iam_instance_profile
    import aws_sdk_guardduty.types.product_codes
    import aws_sdk_guardduty.types.string


class Ec2Instance(TypedDict):
    availability_zone: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The availability zone of the Amazon EC2 instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones\">Availability zones</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    image_description: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The image description of the Amazon EC2 instance.</p>"""
    instance_state: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The state of the Amazon EC2 instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html\">Amazon EC2 instance state changes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_guardduty.types.iam_instance_profile.IamInstanceProfile"
    ]
    instance_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Type of the Amazon EC2 instance.</p>"""
    outpost_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost. This shows applicable Amazon Web Services Outposts instances.</p>"""
    platform: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The platform of the Amazon EC2 instance.</p>"""
    product_codes: NotRequired["aws_sdk_guardduty.types.product_codes.ProductCodes"]
    """<p>The product code of the Amazon EC2 instance.</p>"""
    ec2_network_interface_uids: NotRequired[
        "aws_sdk_guardduty.types.ec2_network_interface_uids.Ec2NetworkInterfaceUids"
    ]
    """<p>The ID of the network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Instance) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "image_description" in value:
        out["imageDescription"] = value["image_description"]
    if "instance_state" in value:
        out["instanceState"] = value["instance_state"]
    if "iam_instance_profile" in value:
        import aws_sdk_guardduty.types.iam_instance_profile

        out["IamInstanceProfile"] = (
            aws_sdk_guardduty.types.iam_instance_profile.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "outpost_arn" in value:
        out["outpostArn"] = value["outpost_arn"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "product_codes" in value:
        import aws_sdk_guardduty.types.product_codes

        out["productCodes"] = aws_sdk_guardduty.types.product_codes.serialize_json(
            value["product_codes"]
        )
    if "ec2_network_interface_uids" in value:
        import aws_sdk_guardduty.types.ec2_network_interface_uids

        out["ec2NetworkInterfaceUids"] = (
            aws_sdk_guardduty.types.ec2_network_interface_uids.serialize_json(
                value["ec2_network_interface_uids"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ec2Instance:
    out: Ec2Instance = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "imageDescription" in data:
        out["image_description"] = data["imageDescription"]
    if "instanceState" in data:
        out["instance_state"] = data["instanceState"]
    if "IamInstanceProfile" in data:
        import aws_sdk_guardduty.types.iam_instance_profile

        out["iam_instance_profile"] = (
            aws_sdk_guardduty.types.iam_instance_profile.deserialize_json(
                data["IamInstanceProfile"]
            )
        )
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "outpostArn" in data:
        out["outpost_arn"] = data["outpostArn"]
    if "platform" in data:
        out["platform"] = data["platform"]
    if "productCodes" in data:
        import aws_sdk_guardduty.types.product_codes

        out["product_codes"] = aws_sdk_guardduty.types.product_codes.deserialize_json(
            data["productCodes"]
        )
    if "ec2NetworkInterfaceUids" in data:
        import aws_sdk_guardduty.types.ec2_network_interface_uids

        out["ec2_network_interface_uids"] = (
            aws_sdk_guardduty.types.ec2_network_interface_uids.deserialize_json(
                data["ec2NetworkInterfaceUids"]
            )
        )
    return out
