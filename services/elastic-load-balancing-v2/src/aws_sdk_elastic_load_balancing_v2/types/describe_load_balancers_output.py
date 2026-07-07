"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeLoadBalancersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancers
    import aws_sdk_elastic_load_balancing_v2.types.marker


class DescribeLoadBalancersOutput(TypedDict, closed=True):
    load_balancers: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancers.LoadBalancers"
    ]
    """<p>Information about the load balancers.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancersOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancers" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancers

        aws_sdk_elastic_load_balancing_v2.types.load_balancers.serialize_query(
            value["load_balancers"], pairs, f"{prefix}.LoadBalancers"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeLoadBalancersOutput:
    out: DescribeLoadBalancersOutput = {}  # type: ignore[typeddict-item]
    child_load_balancers = el.find("LoadBalancers")
    if child_load_balancers is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancers

        out["load_balancers"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancers.deserialize_query(
                child_load_balancers
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
