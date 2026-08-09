"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.next_token
    import capo_ec2.types.traffic_mirror_target_id_list
    import capo_ec2.types.traffic_mirroring_max_results


class DescribeTrafficMirrorTargetsRequest(TypedDict, closed=True):
    traffic_mirror_target_ids: NotRequired[
        "capo_ec2.types.traffic_mirror_target_id_list.TrafficMirrorTargetIdList"
    ]
    """<p>The ID of the Traffic Mirror targets.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>description</code>: The Traffic Mirror target description.</p> </li> <li> <p> <code>network-interface-id</code>: The ID of the Traffic Mirror session network interface.</p> </li> <li> <p> <code>network-load-balancer-arn</code>: The Amazon Resource Name (ARN) of the Network Load Balancer that is associated with the session.</p> </li> <li> <p> <code>owner-id</code>: The ID of the account that owns the Traffic Mirror session.</p> </li> <li> <p> <code>traffic-mirror-target-id</code>: The ID of the Traffic Mirror target.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.traffic_mirroring_max_results.TrafficMirroringMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorTargetsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_target_ids" in value:
        import capo_ec2.types.traffic_mirror_target_id_list

        capo_ec2.types.traffic_mirror_target_id_list.serialize_ec2_query(
            value["traffic_mirror_target_ids"],
            pairs,
            f"{key_prefix}TrafficMirrorTargetId",
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


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorTargetsRequest:
    out: DescribeTrafficMirrorTargetsRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_target_ids = el.find("TrafficMirrorTargetId")
    if child_traffic_mirror_target_ids is not None:
        import capo_ec2.types.traffic_mirror_target_id_list

        out["traffic_mirror_target_ids"] = (
            capo_ec2.types.traffic_mirror_target_id_list.deserialize_ec2_query(
                child_traffic_mirror_target_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
