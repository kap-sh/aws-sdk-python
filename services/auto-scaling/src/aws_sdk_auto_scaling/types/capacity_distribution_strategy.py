"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityDistributionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

CapacityDistributionStrategy: TypeAlias = Literal[
    "balanced-only",
    "balanced-best-effort",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "balanced-only",
        "balanced-best-effort",
    )
)


def to_query_text(value: CapacityDistributionStrategy) -> str:
    return value


def from_query_text(text: str) -> CapacityDistributionStrategy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityDistributionStrategy value: {text!r}"
        )
    return cast(CapacityDistributionStrategy, text)


def serialize_query(
    value: CapacityDistributionStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CapacityDistributionStrategy:
    return from_query_text(el.text or "")
