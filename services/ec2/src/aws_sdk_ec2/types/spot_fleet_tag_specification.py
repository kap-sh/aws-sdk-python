"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetTagSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type
    import aws_sdk_ec2.types.tag_list


class SpotFleetTagSpecification(TypedDict):
    resource_type: NotRequired["aws_sdk_ec2.types.resource_type.ResourceType"]
    """<p>The type of resource. Currently, the only resource type that is supported is <code>instance</code>. To tag the Spot Fleet request on creation, use the <code>TagSpecifications</code> parameter in <code> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html\">SpotFleetRequestConfigData</a> </code>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
