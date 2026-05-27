"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorFilterRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.traffic_direction
    import aws_sdk_ec2.types.traffic_mirror_filter_id
    import aws_sdk_ec2.types.traffic_mirror_port_range_request
    import aws_sdk_ec2.types.traffic_mirror_rule_action


class CreateTrafficMirrorFilterRuleRequest(TypedDict):
    traffic_mirror_filter_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the filter that this rule is associated with.</p>"""
    traffic_direction: NotRequired[
        "aws_sdk_ec2.types.traffic_direction.TrafficDirection"
    ]
    """<p>The type of traffic.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.</p>"""
    rule_action: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_rule_action.TrafficMirrorRuleAction"
    ]
    """<p>The action to take on the filtered traffic.</p>"""
    destination_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The destination port range.</p>"""
    source_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The source port range.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The protocol, for example UDP, to assign to the Traffic Mirror rule.</p> <p>For information about the protocol value, see <a href=\"https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a> on the Internet Assigned Numbers Authority (IANA) website.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block to assign to the Traffic Mirror rule.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block to assign to the Traffic Mirror rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror rule.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Traffic Mirroring tags specifications.</p>"""
