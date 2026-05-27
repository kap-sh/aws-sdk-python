"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeOffering``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.location
    import aws_sdk_ec2.types.location_type


class InstanceTypeOffering(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    location_type: NotRequired["aws_sdk_ec2.types.location_type.LocationType"]
    """<p>The location type.</p>"""
    location: NotRequired["aws_sdk_ec2.types.location.Location"]
    """<p>The identifier for the location. This depends on the location type. For example, if the location type is <code>region</code>, the location is the Region code (for example, <code>us-east-2</code>.)</p>"""
