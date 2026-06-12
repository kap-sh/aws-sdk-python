"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroupIpAddressTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TargetGroupIpAddressTypeEnum: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


def to_query_text(value: TargetGroupIpAddressTypeEnum) -> str:
    return value


def from_query_text(text: str) -> TargetGroupIpAddressTypeEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TargetGroupIpAddressTypeEnum value: {text!r}"
        )
    return cast(TargetGroupIpAddressTypeEnum, text)


def serialize_query(
    value: TargetGroupIpAddressTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetGroupIpAddressTypeEnum:
    return from_query_text(el.text or "")
