"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeListenersInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.listener_arns
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.page_size


class DescribeListenersInput(TypedDict):
    load_balancer_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    listener_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_arns.ListenerArns"
    ]
    """<p>The Amazon Resource Names (ARN) of the listeners.</p>"""
    marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["aws_sdk_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeListenersInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "listener_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.listener_arns

        aws_sdk_elastic_load_balancing_v2.types.listener_arns.serialize_query(
            value["listener_arns"], pairs, f"{prefix}.ListenerArns"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeListenersInput:
    out: DescribeListenersInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_listener_arns = el.find("ListenerArns")
    if child_listener_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.listener_arns

        out["listener_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.listener_arns.deserialize_query(
                child_listener_arns
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
