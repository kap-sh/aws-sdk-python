"""Generated from Smithy shape ``com.amazonaws.cloudformation#AnnotationSeverityLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

AnnotationSeverityLevel: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFORMATIONAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    )
)


def to_query_text(value: AnnotationSeverityLevel) -> str:
    return value


def from_query_text(text: str) -> AnnotationSeverityLevel:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AnnotationSeverityLevel value: {text!r}")
    return cast(AnnotationSeverityLevel, text)


def serialize_query(
    value: AnnotationSeverityLevel, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnnotationSeverityLevel:
    return from_query_text(el.text or "")
