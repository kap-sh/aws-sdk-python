"""Generated from Smithy shape ``com.amazonaws.cloudformation#DriftIgnoredReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

DriftIgnoredReason: TypeAlias = Literal[
    "MANAGED_BY_AWS",
    "WRITE_ONLY_PROPERTY",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED_BY_AWS",
        "WRITE_ONLY_PROPERTY",
    )
)


def to_query_text(value: DriftIgnoredReason) -> str:
    return value


def from_query_text(text: str) -> DriftIgnoredReason:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DriftIgnoredReason value: {text!r}")
    return cast(DriftIgnoredReason, text)


def serialize_query(
    value: DriftIgnoredReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DriftIgnoredReason:
    return from_query_text(el.text or "")
