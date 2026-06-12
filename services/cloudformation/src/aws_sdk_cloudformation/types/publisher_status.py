"""Generated from Smithy shape ``com.amazonaws.cloudformation#PublisherStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

PublisherStatus: TypeAlias = Literal[
    "VERIFIED",
    "UNVERIFIED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERIFIED",
        "UNVERIFIED",
    )
)


def to_query_text(value: PublisherStatus) -> str:
    return value


def from_query_text(text: str) -> PublisherStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PublisherStatus value: {text!r}")
    return cast(PublisherStatus, text)


def serialize_query(
    value: PublisherStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PublisherStatus:
    return from_query_text(el.text or "")
