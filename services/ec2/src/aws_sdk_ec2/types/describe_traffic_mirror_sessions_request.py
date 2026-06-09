"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.traffic_mirror_session_id_list
    import aws_sdk_ec2.types.traffic_mirroring_max_results


class DescribeTrafficMirrorSessionsRequest(TypedDict):
    traffic_mirror_session_ids: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session_id_list.TrafficMirrorSessionIdList"
    ]
    """<p>The ID of the Traffic Mirror session.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>description</code>: The Traffic Mirror session description.</p> </li> <li> <p> <code>network-interface-id</code>: The ID of the Traffic Mirror session network interface.</p> </li> <li> <p> <code>owner-id</code>: The ID of the account that owns the Traffic Mirror session.</p> </li> <li> <p> <code>packet-length</code>: The assigned number of packets to mirror. </p> </li> <li> <p> <code>session-number</code>: The assigned session number. </p> </li> <li> <p> <code>traffic-mirror-filter-id</code>: The ID of the Traffic Mirror filter.</p> </li> <li> <p> <code>traffic-mirror-session-id</code>: The ID of the Traffic Mirror session.</p> </li> <li> <p> <code>traffic-mirror-target-id</code>: The ID of the Traffic Mirror target.</p> </li> <li> <p> <code>virtual-network-id</code>: The virtual network ID of the Traffic Mirror session.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.traffic_mirroring_max_results.TrafficMirroringMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorSessionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_session_ids" in value:
        import aws_sdk_ec2.types.traffic_mirror_session_id_list

        aws_sdk_ec2.types.traffic_mirror_session_id_list.serialize_ec2_query(
            value["traffic_mirror_session_ids"],
            pairs,
            f"{prefix}.TrafficMirrorSessionIds",
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorSessionsRequest:
    out: DescribeTrafficMirrorSessionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("TrafficMirrorSessionIds") is not None:
        import aws_sdk_ec2.types.traffic_mirror_session_id_list

        out["traffic_mirror_session_ids"] = (
            aws_sdk_ec2.types.traffic_mirror_session_id_list.deserialize_ec2_query(
                el, "TrafficMirrorSessionIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
