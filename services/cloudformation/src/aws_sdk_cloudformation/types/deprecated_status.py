"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeprecatedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

DeprecatedStatus: TypeAlias = Literal[
    "LIVE",
    "DEPRECATED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIVE",
        "DEPRECATED",
    )
)


def to_query_text(value: DeprecatedStatus) -> str:
    return value


def from_query_text(text: str) -> DeprecatedStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DeprecatedStatus value: {text!r}")
    return cast(DeprecatedStatus, text)


def serialize_query(
    value: DeprecatedStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeprecatedStatus:
    return from_query_text(el.text or "")
