"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#EnablePrefixForIpv6SourceNatEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

EnablePrefixForIpv6SourceNatEnum: TypeAlias = Literal[
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


def to_query_text(value: EnablePrefixForIpv6SourceNatEnum) -> str:
    return value


def from_query_text(text: str) -> EnablePrefixForIpv6SourceNatEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown EnablePrefixForIpv6SourceNatEnum value: {text!r}"
        )
    return cast(EnablePrefixForIpv6SourceNatEnum, text)


def serialize_query(
    value: EnablePrefixForIpv6SourceNatEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnablePrefixForIpv6SourceNatEnum:
    return from_query_text(el.text or "")
