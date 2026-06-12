"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerSchemeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

LoadBalancerSchemeEnum: TypeAlias = Literal[
    "internet-facing",
    "internal",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "internet-facing",
        "internal",
    )
)


def to_query_text(value: LoadBalancerSchemeEnum) -> str:
    return value


def from_query_text(text: str) -> LoadBalancerSchemeEnum:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LoadBalancerSchemeEnum value: {text!r}")
    return cast(LoadBalancerSchemeEnum, text)


def serialize_query(
    value: LoadBalancerSchemeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LoadBalancerSchemeEnum:
    return from_query_text(el.text or "")
