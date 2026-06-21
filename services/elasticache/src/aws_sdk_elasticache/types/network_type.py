"""Generated from Smithy shape ``com.amazonaws.elasticache#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

NetworkType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dual_stack",
]


# --- awsQuery ser/de ---
def to_query_text(value: NetworkType) -> str:
    return value


def from_query_text(text: str) -> NetworkType:
    return cast(NetworkType, text)


def serialize_query(
    value: NetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NetworkType:
    return from_query_text(el.text or "")
