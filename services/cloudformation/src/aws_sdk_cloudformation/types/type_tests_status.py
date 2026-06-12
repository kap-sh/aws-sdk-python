"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeTestsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

TypeTestsStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "IN_PROGRESS",
    "NOT_TESTED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "IN_PROGRESS",
        "NOT_TESTED",
    )
)


def to_query_text(value: TypeTestsStatus) -> str:
    return value


def from_query_text(text: str) -> TypeTestsStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TypeTestsStatus value: {text!r}")
    return cast(TypeTestsStatus, text)


def serialize_query(
    value: TypeTestsStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TypeTestsStatus:
    return from_query_text(el.text or "")
