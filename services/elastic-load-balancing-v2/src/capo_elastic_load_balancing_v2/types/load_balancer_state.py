"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.load_balancer_state_enum
    import capo_elastic_load_balancing_v2.types.state_reason


class LoadBalancerState(TypedDict, closed=True):
    code: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_state_enum.LoadBalancerStateEnum"
    ]
    """<p>The state code. The initial state of the load balancer is <code>provisioning</code>. After the load balancer is fully set up and ready to route traffic, its state is <code>active</code>. If load balancer is routing traffic but does not have the resources it needs to scale, its state is<code>active_impaired</code>. If the load balancer could not be set up, its state is <code>failed</code>.</p>"""
    reason: NotRequired["capo_elastic_load_balancing_v2.types.state_reason.StateReason"]
    """<p>A description of the state.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        import capo_elastic_load_balancing_v2.types.load_balancer_state_enum

        capo_elastic_load_balancing_v2.types.load_balancer_state_enum.serialize_query(
            value["code"], pairs, f"{key_prefix}Code"
        )
    if "reason" in value:
        pairs.append((f"{key_prefix}Reason", str(value["reason"])))


def deserialize_query(el: Element) -> LoadBalancerState:
    out: LoadBalancerState = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import capo_elastic_load_balancing_v2.types.load_balancer_state_enum

        out["code"] = (
            capo_elastic_load_balancing_v2.types.load_balancer_state_enum.deserialize_query(
                child_code
            )
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
