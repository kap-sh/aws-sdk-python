"""Generated from Smithy shape ``com.amazonaws.cloudformation#CallAs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

CallAs: TypeAlias = Literal[
    "SELF",
    "DELEGATED_ADMIN",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "DELEGATED_ADMIN",
    )
)


def to_query_text(value: CallAs) -> str:
    return value


def from_query_text(text: str) -> CallAs:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CallAs value: {text!r}")
    return cast(CallAs, text)


def serialize_query(value: CallAs, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CallAs:
    return from_query_text(el.text or "")
