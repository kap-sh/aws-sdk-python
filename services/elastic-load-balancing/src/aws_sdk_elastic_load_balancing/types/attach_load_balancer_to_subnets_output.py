"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AttachLoadBalancerToSubnetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.subnets


class AttachLoadBalancerToSubnetsOutput(TypedDict, closed=True):
    subnets: NotRequired["aws_sdk_elastic_load_balancing.types.subnets.Subnets"]
    """<p>The IDs of the subnets attached to the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachLoadBalancerToSubnetsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnets" in value:
        import aws_sdk_elastic_load_balancing.types.subnets

        aws_sdk_elastic_load_balancing.types.subnets.serialize_query(
            value["subnets"], pairs, f"{prefix}.Subnets"
        )


def deserialize_query(el: Element) -> AttachLoadBalancerToSubnetsOutput:
    out: AttachLoadBalancerToSubnetsOutput = {}  # type: ignore[typeddict-item]
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import aws_sdk_elastic_load_balancing.types.subnets

        out["subnets"] = aws_sdk_elastic_load_balancing.types.subnets.deserialize_query(
            child_subnets
        )
    return out
