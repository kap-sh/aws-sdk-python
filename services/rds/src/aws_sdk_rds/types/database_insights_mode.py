"""Generated from Smithy shape ``com.amazonaws.rds#DatabaseInsightsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

DatabaseInsightsMode: TypeAlias = Literal[
    "standard",
    "advanced",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "advanced",
    )
)


def to_query_text(value: DatabaseInsightsMode) -> str:
    return value


def from_query_text(text: str) -> DatabaseInsightsMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DatabaseInsightsMode value: {text!r}")
    return cast(DatabaseInsightsMode, text)


def serialize_query(
    value: DatabaseInsightsMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DatabaseInsightsMode:
    return from_query_text(el.text or "")
