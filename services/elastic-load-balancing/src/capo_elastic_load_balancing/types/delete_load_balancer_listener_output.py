"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DeleteLoadBalancerListenerOutput``."""

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element


class DeleteLoadBalancerListenerOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLoadBalancerListenerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteLoadBalancerListenerOutput:
    out: DeleteLoadBalancerListenerOutput = {}  # type: ignore[typeddict-item]
    return out
