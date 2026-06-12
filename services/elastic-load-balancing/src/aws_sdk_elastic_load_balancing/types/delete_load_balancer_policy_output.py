"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DeleteLoadBalancerPolicyOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class DeleteLoadBalancerPolicyOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLoadBalancerPolicyOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteLoadBalancerPolicyOutput:
    out: DeleteLoadBalancerPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
