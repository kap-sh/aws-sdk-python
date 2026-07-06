"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteLoadBalancerOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class DeleteLoadBalancerOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLoadBalancerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteLoadBalancerOutput:
    out: DeleteLoadBalancerOutput = {}  # type: ignore[typeddict-item]
    return out
