"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeLoadBalancerTargetGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.load_balancer_target_group_states
    import aws_sdk_auto_scaling.types.xml_string


class DescribeLoadBalancerTargetGroupsResponse(TypedDict):
    load_balancer_target_groups: NotRequired[
        "aws_sdk_auto_scaling.types.load_balancer_target_group_states.LoadBalancerTargetGroupStates"
    ]
    """<p>Information about the target groups.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerTargetGroupsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "load_balancer_target_groups" in value:
        import aws_sdk_auto_scaling.types.load_balancer_target_group_states

        aws_sdk_auto_scaling.types.load_balancer_target_group_states.serialize_query(
            value["load_balancer_target_groups"],
            pairs,
            f"{prefix}.LoadBalancerTargetGroups",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeLoadBalancerTargetGroupsResponse:
    out: DescribeLoadBalancerTargetGroupsResponse = {}  # type: ignore[typeddict-item]
    child_load_balancer_target_groups = el.find("LoadBalancerTargetGroups")
    if child_load_balancer_target_groups is not None:
        import aws_sdk_auto_scaling.types.load_balancer_target_group_states

        out["load_balancer_target_groups"] = (
            aws_sdk_auto_scaling.types.load_balancer_target_group_states.deserialize_query(
                child_load_balancer_target_groups
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
