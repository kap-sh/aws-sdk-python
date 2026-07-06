"""Generated from Smithy shape ``com.amazonaws.gamelift#EC2InstanceLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.ec2_instance_type
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.whole_number


class EC2InstanceLimit(TypedDict, closed=True):
    ec2_instance_type: NotRequired[
        "aws_sdk_gamelift.types.ec2_instance_type.EC2InstanceType"
    ]
    r"""<p>The name of an Amazon EC2 instance type. See <a href=\"http://aws.amazon.com/ec2/instance-types/\">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions. </p>"""
    current_instances: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>The number of instances for the specified type and location that are currently being used by the Amazon Web Services account. </p>"""
    instance_limit: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>The number of instances that is allowed for the specified instance type and location.</p>"""
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>An Amazon Web Services Region code, such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceLimit) -> dict:
    out: dict = {}
    if "ec2_instance_type" in value:
        import aws_sdk_gamelift.types.ec2_instance_type

        out["EC2InstanceType"] = (
            aws_sdk_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
                value["ec2_instance_type"]
            )
        )
    if "current_instances" in value:
        out["CurrentInstances"] = value["current_instances"]
    if "instance_limit" in value:
        out["InstanceLimit"] = value["instance_limit"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceLimit:
    out: EC2InstanceLimit = {}  # type: ignore[typeddict-item]
    if "EC2InstanceType" in data:
        import aws_sdk_gamelift.types.ec2_instance_type

        out["ec2_instance_type"] = (
            aws_sdk_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
                data["EC2InstanceType"]
            )
        )
    if "CurrentInstances" in data:
        out["current_instances"] = data["CurrentInstances"]
    if "InstanceLimit" in data:
        out["instance_limit"] = data["InstanceLimit"]
    if "Location" in data:
        out["location"] = data["Location"]
    return out
