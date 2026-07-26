"""Generated from Smithy shape ``com.amazonaws.rds#EndpointNetworkType``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

EndpointNetworkType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
    "DUAL",
]


# --- awsQuery ser/de ---
def to_query_text(value: EndpointNetworkType) -> str:
    return value


def from_query_text(text: str) -> EndpointNetworkType:
    return cast(EndpointNetworkType, text)


def serialize_query(
    value: EndpointNetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EndpointNetworkType:
    return from_query_text(el.text or "")
