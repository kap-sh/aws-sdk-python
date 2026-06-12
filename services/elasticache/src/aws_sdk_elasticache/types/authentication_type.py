"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "password",
    "no-password",
    "iam",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "password",
        "no-password",
        "iam",
    )
)


def to_query_text(value: AuthenticationType) -> str:
    return value


def from_query_text(text: str) -> AuthenticationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {text!r}")
    return cast(AuthenticationType, text)


def serialize_query(
    value: AuthenticationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthenticationType:
    return from_query_text(el.text or "")
