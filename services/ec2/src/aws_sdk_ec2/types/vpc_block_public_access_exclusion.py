"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway_exclusion_mode
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_state


class VpcBlockPublicAccessExclusion(TypedDict):
    exclusion_id: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
    ]
    """<p>The ID of the exclusion.</p>"""
    internet_gateway_exclusion_mode: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_exclusion_mode.InternetGatewayExclusionMode"
    ]
    """<p>The exclusion mode for internet gateway traffic.</p> <ul> <li> <p> <code>allow-bidirectional</code>: Allow all internet traffic to and from the excluded VPCs and subnets.</p> </li> <li> <p> <code>allow-egress</code>: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.</p> </li> </ul>"""
    resource_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the exclusion.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_state.VpcBlockPublicAccessExclusionState"
    ]
    """<p>The state of the exclusion.</p>"""
    reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current exclusion state.</p>"""
    creation_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>When the exclusion was created.</p>"""
    last_update_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>When the exclusion was last updated.</p>"""
    deletion_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>When the exclusion was deleted.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
