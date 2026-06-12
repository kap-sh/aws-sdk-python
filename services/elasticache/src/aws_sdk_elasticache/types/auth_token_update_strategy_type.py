"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthTokenUpdateStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

AuthTokenUpdateStrategyType: TypeAlias = Literal[
    "SET",
    "ROTATE",
    "DELETE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SET",
        "ROTATE",
        "DELETE",
    )
)


def to_query_text(value: AuthTokenUpdateStrategyType) -> str:
    return value


def from_query_text(text: str) -> AuthTokenUpdateStrategyType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown AuthTokenUpdateStrategyType value: {text!r}"
        )
    return cast(AuthTokenUpdateStrategyType, text)


def serialize_query(
    value: AuthTokenUpdateStrategyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthTokenUpdateStrategyType:
    return from_query_text(el.text or "")
