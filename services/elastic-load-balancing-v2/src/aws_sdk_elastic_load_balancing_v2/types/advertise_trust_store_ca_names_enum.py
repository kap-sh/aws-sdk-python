"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AdvertiseTrustStoreCaNamesEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

AdvertiseTrustStoreCaNamesEnum: TypeAlias = Literal[
    "on",
    "off",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "on",
        "off",
    )
)


def to_query_text(value: AdvertiseTrustStoreCaNamesEnum) -> str:
    return value


def from_query_text(text: str) -> AdvertiseTrustStoreCaNamesEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown AdvertiseTrustStoreCaNamesEnum value: {text!r}"
        )
    return cast(AdvertiseTrustStoreCaNamesEnum, text)


def serialize_query(
    value: AdvertiseTrustStoreCaNamesEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AdvertiseTrustStoreCaNamesEnum:
    return from_query_text(el.text or "")
