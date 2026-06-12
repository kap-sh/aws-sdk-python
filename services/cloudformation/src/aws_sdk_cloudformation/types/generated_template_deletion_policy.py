"""Generated from Smithy shape ``com.amazonaws.cloudformation#GeneratedTemplateDeletionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

GeneratedTemplateDeletionPolicy: TypeAlias = Literal[
    "DELETE",
    "RETAIN",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE",
        "RETAIN",
    )
)


def to_query_text(value: GeneratedTemplateDeletionPolicy) -> str:
    return value


def from_query_text(text: str) -> GeneratedTemplateDeletionPolicy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown GeneratedTemplateDeletionPolicy value: {text!r}"
        )
    return cast(GeneratedTemplateDeletionPolicy, text)


def serialize_query(
    value: GeneratedTemplateDeletionPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GeneratedTemplateDeletionPolicy:
    return from_query_text(el.text or "")
