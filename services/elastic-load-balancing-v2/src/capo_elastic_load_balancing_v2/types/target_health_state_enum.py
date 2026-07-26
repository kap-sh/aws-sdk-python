"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetHealthStateEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

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
def to_query_text(value: TargetHealthStateEnum) -> str:
    return value


def from_query_text(text: str) -> TargetHealthStateEnum:
    return cast(TargetHealthStateEnum, text)


def serialize_query(
    value: TargetHealthStateEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetHealthStateEnum:
    return from_query_text(el.text or "")
