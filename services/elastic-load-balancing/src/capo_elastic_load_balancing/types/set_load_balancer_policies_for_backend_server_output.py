"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerPoliciesForBackendServerOutput``."""

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element


class SetLoadBalancerPoliciesForBackendServerOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerPoliciesForBackendServerOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> SetLoadBalancerPoliciesForBackendServerOutput:
    out: SetLoadBalancerPoliciesForBackendServerOutput = {}  # type: ignore[typeddict-item]
    return out
