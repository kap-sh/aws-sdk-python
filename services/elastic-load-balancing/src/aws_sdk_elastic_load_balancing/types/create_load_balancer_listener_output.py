"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancerListenerOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class CreateLoadBalancerListenerOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerListenerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateLoadBalancerListenerOutput:
    out: CreateLoadBalancerListenerOutput = {}  # type: ignore[typeddict-item]
    return out
