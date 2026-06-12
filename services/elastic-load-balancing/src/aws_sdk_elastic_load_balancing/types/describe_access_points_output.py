"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeAccessPointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.load_balancer_descriptions
    import aws_sdk_elastic_load_balancing.types.marker


class DescribeAccessPointsOutput(TypedDict):
    load_balancer_descriptions: NotRequired[
        "aws_sdk_elastic_load_balancing.types.load_balancer_descriptions.LoadBalancerDescriptions"
    ]
    """<p>Information about the load balancers.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing.types.marker.Marker"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccessPointsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_descriptions" in value:
        import aws_sdk_elastic_load_balancing.types.load_balancer_descriptions

        aws_sdk_elastic_load_balancing.types.load_balancer_descriptions.serialize_query(
            value["load_balancer_descriptions"],
            pairs,
            f"{prefix}.LoadBalancerDescriptions",
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeAccessPointsOutput:
    out: DescribeAccessPointsOutput = {}  # type: ignore[typeddict-item]
    child_load_balancer_descriptions = el.find("LoadBalancerDescriptions")
    if child_load_balancer_descriptions is not None:
        import aws_sdk_elastic_load_balancing.types.load_balancer_descriptions

        out["load_balancer_descriptions"] = (
            aws_sdk_elastic_load_balancing.types.load_balancer_descriptions.deserialize_query(
                child_load_balancer_descriptions
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
