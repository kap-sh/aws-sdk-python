"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFilterRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.next_token
    import capo_ec2.types.traffic_mirror_filter_id
    import capo_ec2.types.traffic_mirror_filter_rule_id_list
    import capo_ec2.types.traffic_mirroring_max_results


class DescribeTrafficMirrorFilterRulesRequest(TypedDict, closed=True):
    traffic_mirror_filter_rule_ids: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_rule_id_list.TrafficMirrorFilterRuleIdList"
    ]
    """<p>Traffic filter rule IDs.</p>"""
    traffic_mirror_filter_id: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>Traffic filter ID.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>Traffic mirror filters.</p> <ul> <li> <p> <code>traffic-mirror-filter-rule-id</code>: The ID of the Traffic Mirror rule.</p> </li> <li> <p> <code>traffic-mirror-filter-id</code>: The ID of the filter that this rule is associated with.</p> </li> <li> <p> <code>rule-number</code>: The number of the Traffic Mirror rule.</p> </li> <li> <p> <code>rule-action</code>: The action taken on the filtered traffic. Possible actions are <code>accept</code> and <code>reject</code>.</p> </li> <li> <p> <code>traffic-direction</code>: The traffic direction. Possible directions are <code>ingress</code> and <code>egress</code>.</p> </li> <li> <p> <code>protocol</code>: The protocol, for example UDP, assigned to the Traffic Mirror rule.</p> </li> <li> <p> <code>source-cidr-block</code>: The source CIDR block assigned to the Traffic Mirror rule.</p> </li> <li> <p> <code>destination-cidr-block</code>: The destination CIDR block assigned to the Traffic Mirror rule.</p> </li> <li> <p> <code>description</code>: The description of the Traffic Mirror rule.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.traffic_mirroring_max_results.TrafficMirroringMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorFilterRulesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_filter_rule_ids" in value:
        import capo_ec2.types.traffic_mirror_filter_rule_id_list

        capo_ec2.types.traffic_mirror_filter_rule_id_list.serialize_ec2_query(
            value["traffic_mirror_filter_rule_ids"],
            pairs,
            f"{key_prefix}TrafficMirrorFilterRuleId",
        )
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterId",
                str(value["traffic_mirror_filter_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorFilterRulesRequest:
    out: DescribeTrafficMirrorFilterRulesRequest = {}  # type: ignore[typeddict-item]
    if el.find("TrafficMirrorFilterRuleId") is not None:
        import capo_ec2.types.traffic_mirror_filter_rule_id_list

        out["traffic_mirror_filter_rule_ids"] = (
            capo_ec2.types.traffic_mirror_filter_rule_id_list.deserialize_ec2_query(
                el, "TrafficMirrorFilterRuleId"
            )
        )
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
