"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachLoadBalancerTargetGroupsResultType``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class DetachLoadBalancerTargetGroupsResultType(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachLoadBalancerTargetGroupsResultType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DetachLoadBalancerTargetGroupsResultType:
    out: DetachLoadBalancerTargetGroupsResultType = {}  # type: ignore[typeddict-item]
    return out
