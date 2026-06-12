"""Generated from Smithy shape ``com.amazonaws.cloudformation#Category``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

Category: TypeAlias = Literal[
    "REGISTERED",
    "ACTIVATED",
    "THIRD_PARTY",
    "AWS_TYPES",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERED",
        "ACTIVATED",
        "THIRD_PARTY",
        "AWS_TYPES",
    )
)


def to_query_text(value: Category) -> str:
    return value


def from_query_text(text: str) -> Category:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Category value: {text!r}")
    return cast(Category, text)


def serialize_query(value: Category, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Category:
    return from_query_text(el.text or "")
