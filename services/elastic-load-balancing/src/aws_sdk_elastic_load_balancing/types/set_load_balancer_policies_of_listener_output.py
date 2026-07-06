"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerPoliciesOfListenerOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class SetLoadBalancerPoliciesOfListenerOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerPoliciesOfListenerOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> SetLoadBalancerPoliciesOfListenerOutput:
    out: SetLoadBalancerPoliciesOfListenerOutput = {}  # type: ignore[typeddict-item]
    return out
