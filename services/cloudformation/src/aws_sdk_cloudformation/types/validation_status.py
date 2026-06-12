"""Generated from Smithy shape ``com.amazonaws.cloudformation#ValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ValidationStatus: TypeAlias = Literal[
    "FAILED",
    "SKIPPED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SKIPPED",
    )
)


def to_query_text(value: ValidationStatus) -> str:
    return value


def from_query_text(text: str) -> ValidationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ValidationStatus value: {text!r}")
    return cast(ValidationStatus, text)


def serialize_query(
    value: ValidationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ValidationStatus:
    return from_query_text(el.text or "")
