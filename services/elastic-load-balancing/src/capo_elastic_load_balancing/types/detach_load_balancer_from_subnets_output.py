"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DetachLoadBalancerFromSubnetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.subnets


class DetachLoadBalancerFromSubnetsOutput(TypedDict, closed=True):
    subnets: NotRequired["capo_elastic_load_balancing.types.subnets.Subnets"]
    """<p>The IDs of the remaining subnets for the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachLoadBalancerFromSubnetsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "subnets" in value:
        import capo_elastic_load_balancing.types.subnets

        capo_elastic_load_balancing.types.subnets.serialize_query(
            value["subnets"], pairs, f"{prefix}.Subnets"
        )


def deserialize_query(el: Element) -> DetachLoadBalancerFromSubnetsOutput:
    out: DetachLoadBalancerFromSubnetsOutput = {}  # type: ignore[typeddict-item]
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_elastic_load_balancing.types.subnets

        out["subnets"] = capo_elastic_load_balancing.types.subnets.deserialize_query(
            child_subnets
        )
    return out
