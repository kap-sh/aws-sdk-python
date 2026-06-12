"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

LoadBalancerTypeEnum: TypeAlias = Literal[
    "application",
    "network",
    "gateway",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "application",
        "network",
        "gateway",
    )
)


def to_query_text(value: LoadBalancerTypeEnum) -> str:
    return value


def from_query_text(text: str) -> LoadBalancerTypeEnum:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LoadBalancerTypeEnum value: {text!r}")
    return cast(LoadBalancerTypeEnum, text)


def serialize_query(
    value: LoadBalancerTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LoadBalancerTypeEnum:
    return from_query_text(el.text or "")
