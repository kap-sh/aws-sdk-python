"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateLoadBalancerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.load_balancers


class CreateLoadBalancerOutput(TypedDict, closed=True):
    load_balancers: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancers.LoadBalancers"
    ]
    """<p>Information about the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancers" in value:
        import capo_elastic_load_balancing_v2.types.load_balancers

        capo_elastic_load_balancing_v2.types.load_balancers.serialize_query(
            value["load_balancers"], pairs, f"{prefix}.LoadBalancers"
        )


def deserialize_query(el: Element) -> CreateLoadBalancerOutput:
    out: CreateLoadBalancerOutput = {}  # type: ignore[typeddict-item]
    child_load_balancers = el.find("LoadBalancers")
    if child_load_balancers is not None:
        import capo_elastic_load_balancing_v2.types.load_balancers

        out["load_balancers"] = (
            capo_elastic_load_balancing_v2.types.load_balancers.deserialize_query(
                child_load_balancers
            )
        )
    return out
