"""Generated from Smithy shape ``com.amazonaws.guardduty#InstanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.iam_instance_profile
    import aws_sdk_guardduty.types.network_interfaces
    import aws_sdk_guardduty.types.product_codes
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags


class InstanceDetails(TypedDict):
    availability_zone: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Availability Zone of the EC2 instance.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_guardduty.types.iam_instance_profile.IamInstanceProfile"
    ]
    """<p>The profile information of the EC2 instance.</p>"""
    image_description: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The image description of the EC2 instance.</p>"""
    image_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The image ID of the EC2 instance.</p>"""
    instance_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the EC2 instance.</p>"""
    instance_state: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The state of the EC2 instance.</p>"""
    instance_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The type of the EC2 instance.</p>"""
    outpost_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost. Only applicable to Amazon Web Services Outposts instances.</p>"""
    launch_time: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The launch time of the EC2 instance.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_guardduty.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>The elastic network interface information of the EC2 instance.</p>"""
    platform: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The platform of the EC2 instance.</p>"""
    product_codes: NotRequired["aws_sdk_guardduty.types.product_codes.ProductCodes"]
    """<p>The product code of the EC2 instance.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>The tags of the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceDetails) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "iam_instance_profile" in value:
        import aws_sdk_guardduty.types.iam_instance_profile

        out["iamInstanceProfile"] = (
            aws_sdk_guardduty.types.iam_instance_profile.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "image_description" in value:
        out["imageDescription"] = value["image_description"]
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "instance_state" in value:
        out["instanceState"] = value["instance_state"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "outpost_arn" in value:
        out["outpostArn"] = value["outpost_arn"]
    if "launch_time" in value:
        out["launchTime"] = value["launch_time"]
    if "network_interfaces" in value:
        import aws_sdk_guardduty.types.network_interfaces

        out["networkInterfaces"] = (
            aws_sdk_guardduty.types.network_interfaces.serialize_json(
                value["network_interfaces"]
            )
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "product_codes" in value:
        import aws_sdk_guardduty.types.product_codes

        out["productCodes"] = aws_sdk_guardduty.types.product_codes.serialize_json(
            value["product_codes"]
        )
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> InstanceDetails:
    out: InstanceDetails = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "iamInstanceProfile" in data:
        import aws_sdk_guardduty.types.iam_instance_profile

        out["iam_instance_profile"] = (
            aws_sdk_guardduty.types.iam_instance_profile.deserialize_json(
                data["iamInstanceProfile"]
            )
        )
    if "imageDescription" in data:
        out["image_description"] = data["imageDescription"]
    if "imageId" in data:
        out["image_id"] = data["imageId"]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "instanceState" in data:
        out["instance_state"] = data["instanceState"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "outpostArn" in data:
        out["outpost_arn"] = data["outpostArn"]
    if "launchTime" in data:
        out["launch_time"] = data["launchTime"]
    if "networkInterfaces" in data:
        import aws_sdk_guardduty.types.network_interfaces

        out["network_interfaces"] = (
            aws_sdk_guardduty.types.network_interfaces.deserialize_json(
                data["networkInterfaces"]
            )
        )
    if "platform" in data:
        out["platform"] = data["platform"]
    if "productCodes" in data:
        import aws_sdk_guardduty.types.product_codes

        out["product_codes"] = aws_sdk_guardduty.types.product_codes.deserialize_json(
            data["productCodes"]
        )
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    return out
