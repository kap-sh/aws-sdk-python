"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveIpamPoolEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

RemoveIpamPoolEnum: TypeAlias = Literal["ipv4",]


# --- awsQuery ser/de ---
def to_query_text(value: RemoveIpamPoolEnum) -> str:
    return value


def from_query_text(text: str) -> RemoveIpamPoolEnum:
    return cast(RemoveIpamPoolEnum, text)


def serialize_query(
    value: RemoveIpamPoolEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RemoveIpamPoolEnum:
    return from_query_text(el.text or "")
