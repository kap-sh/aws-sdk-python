"""Generated from Smithy shape ``com.amazonaws.rds#AuthScheme``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

AuthScheme: TypeAlias = Literal["SECRETS",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("SECRETS",))


def to_query_text(value: AuthScheme) -> str:
    return value


def from_query_text(text: str) -> AuthScheme:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AuthScheme value: {text!r}")
    return cast(AuthScheme, text)


def serialize_query(
    value: AuthScheme, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthScheme:
    return from_query_text(el.text or "")
