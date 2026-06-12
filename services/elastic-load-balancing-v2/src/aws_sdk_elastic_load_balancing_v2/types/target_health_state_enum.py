"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetHealthStateEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TargetHealthStateEnum: TypeAlias = Literal[
    "initial",
    "healthy",
    "unhealthy",
    "unhealthy.draining",
    "unused",
    "draining",
    "unavailable",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "initial",
        "healthy",
        "unhealthy",
        "unhealthy.draining",
        "unused",
        "draining",
        "unavailable",
    )
)


def to_query_text(value: TargetHealthStateEnum) -> str:
    return value


def from_query_text(text: str) -> TargetHealthStateEnum:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TargetHealthStateEnum value: {text!r}")
    return cast(TargetHealthStateEnum, text)


def serialize_query(
    value: TargetHealthStateEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetHealthStateEnum:
    return from_query_text(el.text or "")
