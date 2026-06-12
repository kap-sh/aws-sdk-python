"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TargetTypeEnum: TypeAlias = Literal[
    "instance",
    "ip",
    "lambda",
    "alb",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "instance",
        "ip",
        "lambda",
        "alb",
    )
)


def to_query_text(value: TargetTypeEnum) -> str:
    return value


def from_query_text(text: str) -> TargetTypeEnum:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TargetTypeEnum value: {text!r}")
    return cast(TargetTypeEnum, text)


def serialize_query(
    value: TargetTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetTypeEnum:
    return from_query_text(el.text or "")
