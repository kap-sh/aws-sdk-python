"""Generated from Smithy shape ``com.amazonaws.rds#EndpointNetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

EndpointNetworkType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
    "DUAL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
        "DUAL",
    )
)


def to_query_text(value: EndpointNetworkType) -> str:
    return value


def from_query_text(text: str) -> EndpointNetworkType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EndpointNetworkType value: {text!r}")
    return cast(EndpointNetworkType, text)


def serialize_query(
    value: EndpointNetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EndpointNetworkType:
    return from_query_text(el.text or "")
