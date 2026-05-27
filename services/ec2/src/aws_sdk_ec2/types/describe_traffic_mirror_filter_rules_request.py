"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFilterRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.traffic_mirror_filter_id
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_list
    import aws_sdk_ec2.types.traffic_mirroring_max_results


class DescribeTrafficMirrorFilterRulesRequest(TypedDict):
    traffic_mirror_filter_rule_ids: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_id_list.TrafficMirrorFilterRuleIdList"
    ]
    """<p>Traffic filter rule IDs.</p>"""
    traffic_mirror_filter_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>Traffic filter ID.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Traffic mirror filters.</p> <ul> <li> <p> <code>traffic-mirror-filter-rule-id</code>: The ID of the Traffic Mirror rule.</p> </li> <li> <p> <code>traffic-mirror-filter-id</code>: The ID of the filter that this rule is associated with.</p> </li> <li> <p> <code>rule-number</code>: The number of the Traffic Mirror rule.</p> </li> <li> <p> <code>rule-action</code>: The action taken on the filtered traffic. Possible actions are <code>accept</code> and <code>reject</code>.</p> </li> <li> <p> <code>traffic-direction</code>: The traffic direction. Possible directions are <code>ingress</code> and <code>egress</code>.</p> </li> <li> <p> <code>protocol</code>: The protocol, for example UDP, assigned to the Traffic Mirror rule.</p> </li> <li> <p> <code>source-cidr-block</code>: The source CIDR block assigned to the Traffic Mirror rule.</p> </li> <li> <p> <code>destination-cidr-block</code>: The destination CIDR block assigned to the Traffic Mirror rule.</p> </li> <li> <p> <code>description</code>: The description of the Traffic Mirror rule.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.traffic_mirroring_max_results.TrafficMirroringMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
