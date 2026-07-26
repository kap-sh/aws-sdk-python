"""Generated from Smithy shape ``com.amazonaws.autoscaling#LoadBalancerStates``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.load_balancer_state

LoadBalancerStates: TypeAlias = list[
    "capo_auto_scaling.types.load_balancer_state.LoadBalancerState"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.load_balancer_state

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.load_balancer_state.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerStates:
    import capo_auto_scaling.types.load_balancer_state

    out: LoadBalancerStates = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.load_balancer_state.deserialize_query(child))
    return out


def serialize_query_flat(
    value: LoadBalancerStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.load_balancer_state

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.load_balancer_state.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerStates:
    import capo_auto_scaling.types.load_balancer_state

    out: LoadBalancerStates = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.load_balancer_state.deserialize_query(child))
    return out
