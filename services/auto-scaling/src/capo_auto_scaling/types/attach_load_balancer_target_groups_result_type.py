"""Generated from Smithy shape ``com.amazonaws.autoscaling#AttachLoadBalancerTargetGroupsResultType``."""

from typing_extensions import TypedDict

from capo_auto_scaling._protocol.xml import Element


class AttachLoadBalancerTargetGroupsResultType(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachLoadBalancerTargetGroupsResultType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> AttachLoadBalancerTargetGroupsResultType:
    out: AttachLoadBalancerTargetGroupsResultType = {}  # type: ignore[typeddict-item]
    return out
