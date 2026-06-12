"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

ServiceUpdateSeverity: TypeAlias = Literal[
    "critical",
    "important",
    "medium",
    "low",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "critical",
        "important",
        "medium",
        "low",
    )
)


def to_query_text(value: ServiceUpdateSeverity) -> str:
    return value


def from_query_text(text: str) -> ServiceUpdateSeverity:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceUpdateSeverity value: {text!r}")
    return cast(ServiceUpdateSeverity, text)


def serialize_query(
    value: ServiceUpdateSeverity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ServiceUpdateSeverity:
    return from_query_text(el.text or "")
