"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeLoadBalancersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.load_balancer_states
    import aws_sdk_auto_scaling.types.xml_string


class DescribeLoadBalancersResponse(TypedDict, closed=True):
    load_balancers: NotRequired[
        "aws_sdk_auto_scaling.types.load_balancer_states.LoadBalancerStates"
    ]
    """<p>The load balancers.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancers" in value:
        import aws_sdk_auto_scaling.types.load_balancer_states

        aws_sdk_auto_scaling.types.load_balancer_states.serialize_query(
            value["load_balancers"], pairs, f"{prefix}.LoadBalancers"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeLoadBalancersResponse:
    out: DescribeLoadBalancersResponse = {}  # type: ignore[typeddict-item]
    child_load_balancers = el.find("LoadBalancers")
    if child_load_balancers is not None:
        import aws_sdk_auto_scaling.types.load_balancer_states

        out["load_balancers"] = (
            aws_sdk_auto_scaling.types.load_balancer_states.deserialize_query(
                child_load_balancers
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
