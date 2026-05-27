"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsPath``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.path_filter
    import aws_sdk_ec2.types.protocol
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkInsightsPath(TypedDict):
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""
    network_insights_path_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the path.</p>"""
    created_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time stamp when the path was created.</p>"""
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the destination.</p>"""
    source_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    destination_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""
    source_ip: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the source.</p>"""
    destination_ip: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the destination.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.protocol.Protocol"]
    """<p>The protocol.</p>"""
    destination_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The destination port.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the path.</p>"""
    filter_at_source: NotRequired["aws_sdk_ec2.types.path_filter.PathFilter"]
    """<p>Scopes the analysis to network paths that match specific filters at the source.</p>"""
    filter_at_destination: NotRequired["aws_sdk_ec2.types.path_filter.PathFilter"]
    """<p>Scopes the analysis to network paths that match specific filters at the destination.</p>"""
