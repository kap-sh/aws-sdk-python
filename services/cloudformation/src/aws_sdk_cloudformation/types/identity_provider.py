"""Generated from Smithy shape ``com.amazonaws.cloudformation#IdentityProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

IdentityProvider: TypeAlias = Literal[
    "AWS_Marketplace",
    "GitHub",
    "Bitbucket",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_Marketplace",
        "GitHub",
        "Bitbucket",
    )
)


def to_query_text(value: IdentityProvider) -> str:
    return value


def from_query_text(text: str) -> IdentityProvider:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IdentityProvider value: {text!r}")
    return cast(IdentityProvider, text)


def serialize_query(
    value: IdentityProvider, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IdentityProvider:
    return from_query_text(el.text or "")
