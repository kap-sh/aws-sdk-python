"""Generated from Smithy shape ``com.amazonaws.cloudformation#ConcurrencyMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ConcurrencyMode: TypeAlias = Literal[
    "STRICT_FAILURE_TOLERANCE",
    "SOFT_FAILURE_TOLERANCE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRICT_FAILURE_TOLERANCE",
        "SOFT_FAILURE_TOLERANCE",
    )
)


def to_query_text(value: ConcurrencyMode) -> str:
    return value


def from_query_text(text: str) -> ConcurrencyMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ConcurrencyMode value: {text!r}")
    return cast(ConcurrencyMode, text)


def serialize_query(
    value: ConcurrencyMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConcurrencyMode:
    return from_query_text(el.text or "")
