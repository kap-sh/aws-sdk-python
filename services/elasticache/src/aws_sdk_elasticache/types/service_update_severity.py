"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

ServiceUpdateSeverity: TypeAlias = Literal[
    "critical",
    "important",
    "medium",
    "low",
]


# --- awsQuery ser/de ---
def to_query_text(value: ServiceUpdateSeverity) -> str:
    return value


def from_query_text(text: str) -> ServiceUpdateSeverity:
    return cast(ServiceUpdateSeverity, text)


def serialize_query(
    value: ServiceUpdateSeverity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ServiceUpdateSeverity:
    return from_query_text(el.text or "")
