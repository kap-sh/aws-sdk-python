"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancerPolicyOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class CreateLoadBalancerPolicyOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerPolicyOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateLoadBalancerPolicyOutput:
    out: CreateLoadBalancerPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
