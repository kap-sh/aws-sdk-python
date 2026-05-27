"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsPathRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.network_insights_resource_id
    import aws_sdk_ec2.types.path_request_filter
    import aws_sdk_ec2.types.port
    import aws_sdk_ec2.types.protocol
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateNetworkInsightsPathRequest(TypedDict):
    source_ip: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the source.</p>"""
    destination_ip: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the destination.</p>"""
    source: NotRequired[
        "aws_sdk_ec2.types.network_insights_resource_id.NetworkInsightsResourceId"
    ]
    """<p>The ID or ARN of the source. If the resource is in another account, you must specify an ARN.</p>"""
    destination: NotRequired[
        "aws_sdk_ec2.types.network_insights_resource_id.NetworkInsightsResourceId"
    ]
    """<p>The ID or ARN of the destination. If the resource is in another account, you must specify an ARN.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.protocol.Protocol"]
    """<p>The protocol.</p>"""
    destination_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The destination port.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to add to the path.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
    filter_at_source: NotRequired[
        "aws_sdk_ec2.types.path_request_filter.PathRequestFilter"
    ]
    """<p>Scopes the analysis to network paths that match specific filters at the source. If you specify this parameter, you can't specify the parameters for the source IP address or the destination port.</p>"""
    filter_at_destination: NotRequired[
        "aws_sdk_ec2.types.path_request_filter.PathRequestFilter"
    ]
    """<p>Scopes the analysis to network paths that match specific filters at the destination. If you specify this parameter, you can't specify the parameter for the destination IP address.</p>"""
