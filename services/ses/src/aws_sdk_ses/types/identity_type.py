"""Generated from Smithy shape ``com.amazonaws.ses#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

IdentityType: TypeAlias = Literal[
    "EmailAddress",
    "Domain",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EmailAddress",
        "Domain",
    )
)


def to_query_text(value: IdentityType) -> str:
    return value


def from_query_text(text: str) -> IdentityType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {text!r}")
    return cast(IdentityType, text)


def serialize_query(
    value: IdentityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IdentityType:
    return from_query_text(el.text or "")
