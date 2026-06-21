"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#EnablePrefixForIpv6SourceNatEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

EnablePrefixForIpv6SourceNatEnum: TypeAlias = Literal[
    "on",
    "off",
]


# --- awsQuery ser/de ---
def to_query_text(value: EnablePrefixForIpv6SourceNatEnum) -> str:
    return value


def from_query_text(text: str) -> EnablePrefixForIpv6SourceNatEnum:
    return cast(EnablePrefixForIpv6SourceNatEnum, text)


def serialize_query(
    value: EnablePrefixForIpv6SourceNatEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnablePrefixForIpv6SourceNatEnum:
    return from_query_text(el.text or "")
