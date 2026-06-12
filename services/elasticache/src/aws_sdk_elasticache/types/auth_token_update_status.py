"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthTokenUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

AuthTokenUpdateStatus: TypeAlias = Literal[
    "SETTING",
    "ROTATING",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SETTING",
        "ROTATING",
    )
)


def to_query_text(value: AuthTokenUpdateStatus) -> str:
    return value


def from_query_text(text: str) -> AuthTokenUpdateStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AuthTokenUpdateStatus value: {text!r}")
    return cast(AuthTokenUpdateStatus, text)


def serialize_query(
    value: AuthTokenUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthTokenUpdateStatus:
    return from_query_text(el.text or "")
