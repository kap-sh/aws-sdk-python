"""Generated from Smithy shape ``com.amazonaws.cloudformation#AnnotationSeverityLevel``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

AnnotationSeverityLevel: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- awsQuery ser/de ---
def to_query_text(value: AnnotationSeverityLevel) -> str:
    return value


def from_query_text(text: str) -> AnnotationSeverityLevel:
    return cast(AnnotationSeverityLevel, text)


def serialize_query(
    value: AnnotationSeverityLevel, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnnotationSeverityLevel:
    return from_query_text(el.text or "")
