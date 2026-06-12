"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachLoadBalancersResultType``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class DetachLoadBalancersResultType(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachLoadBalancersResultType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DetachLoadBalancersResultType:
    out: DetachLoadBalancersResultType = {}  # type: ignore[typeddict-item]
    return out
