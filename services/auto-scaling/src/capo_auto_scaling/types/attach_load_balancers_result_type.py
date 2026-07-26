"""Generated from Smithy shape ``com.amazonaws.autoscaling#AttachLoadBalancersResultType``."""

from typing_extensions import TypedDict

from capo_auto_scaling._protocol.xml import Element


class AttachLoadBalancersResultType(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachLoadBalancersResultType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> AttachLoadBalancersResultType:
    out: AttachLoadBalancersResultType = {}  # type: ignore[typeddict-item]
    return out
