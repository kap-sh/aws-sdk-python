"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorTargetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.traffic_mirror_target_set


class DescribeTrafficMirrorTargetsResult(TypedDict, closed=True):
    traffic_mirror_targets: NotRequired[
        "capo_ec2.types.traffic_mirror_target_set.TrafficMirrorTargetSet"
    ]
    """<p>Information about one or more Traffic Mirror targets.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorTargetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_targets" in value:
        import capo_ec2.types.traffic_mirror_target_set

        capo_ec2.types.traffic_mirror_target_set.serialize_ec2_query(
            value["traffic_mirror_targets"],
            pairs,
            f"{key_prefix}TrafficMirrorTargetSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorTargetsResult:
    out: DescribeTrafficMirrorTargetsResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_targets = el.find("trafficMirrorTargetSet")
    if child_traffic_mirror_targets is not None:
        import capo_ec2.types.traffic_mirror_target_set

        out["traffic_mirror_targets"] = (
            capo_ec2.types.traffic_mirror_target_set.deserialize_ec2_query(
                child_traffic_mirror_targets
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
