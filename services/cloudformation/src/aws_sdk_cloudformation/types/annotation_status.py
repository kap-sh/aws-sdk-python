"""Generated from Smithy shape ``com.amazonaws.cloudformation#AnnotationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

AnnotationStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "SKIPPED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "SKIPPED",
    )
)


def to_query_text(value: AnnotationStatus) -> str:
    return value


def from_query_text(text: str) -> AnnotationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AnnotationStatus value: {text!r}")
    return cast(AnnotationStatus, text)


def serialize_query(
    value: AnnotationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnnotationStatus:
    return from_query_text(el.text or "")
