"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityDistributionStrategy``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

CapacityDistributionStrategy: TypeAlias = Literal[
    "balanced-only",
    "balanced-best-effort",
]


# --- awsQuery ser/de ---
def to_query_text(value: CapacityDistributionStrategy) -> str:
    return value


def from_query_text(text: str) -> CapacityDistributionStrategy:
    return cast(CapacityDistributionStrategy, text)


def serialize_query(
    value: CapacityDistributionStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CapacityDistributionStrategy:
    return from_query_text(el.text or "")
