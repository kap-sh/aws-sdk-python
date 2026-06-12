"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerPoliciesForBackendServerOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class SetLoadBalancerPoliciesForBackendServerOutput(TypedDict):
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
