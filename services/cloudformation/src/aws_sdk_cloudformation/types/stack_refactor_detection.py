"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorDetection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackRefactorDetection: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "MANUAL",
    )
)


def to_query_text(value: StackRefactorDetection) -> str:
    return value


def from_query_text(text: str) -> StackRefactorDetection:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackRefactorDetection value: {text!r}")
    return cast(StackRefactorDetection, text)


def serialize_query(
    value: StackRefactorDetection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorDetection:
    return from_query_text(el.text or "")
