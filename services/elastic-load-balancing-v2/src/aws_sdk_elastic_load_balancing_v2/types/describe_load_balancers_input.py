"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeLoadBalancersInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_names
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.page_size


class DescribeLoadBalancersInput(TypedDict):
    load_balancer_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns.LoadBalancerArns"
    ]
    """<p>The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.</p>"""
    names: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_names.LoadBalancerNames"
    ]
    """<p>The names of the load balancers.</p>"""
    marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["aws_sdk_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancersInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns.serialize_query(
            value["load_balancer_arns"], pairs, f"{prefix}.LoadBalancerArns"
        )
    if "names" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_names

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_names.serialize_query(
            value["names"], pairs, f"{prefix}.Names"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeLoadBalancersInput:
    out: DescribeLoadBalancersInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arns = el.find("LoadBalancerArns")
    if child_load_balancer_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns

        out["load_balancer_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns.deserialize_query(
                child_load_balancer_arns
            )
        )
    child_names = el.find("Names")
    if child_names is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_names

        out["names"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_names.deserialize_query(
                child_names
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
