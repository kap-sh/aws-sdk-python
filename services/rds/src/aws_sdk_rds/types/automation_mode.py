"""Generated from Smithy shape ``com.amazonaws.rds#AutomationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

AutomationMode: TypeAlias = Literal[
    "full",
    "all-paused",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "full",
        "all-paused",
    )
)


def to_query_text(value: AutomationMode) -> str:
    return value


def from_query_text(text: str) -> AutomationMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AutomationMode value: {text!r}")
    return cast(AutomationMode, text)


def serialize_query(
    value: AutomationMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AutomationMode:
    return from_query_text(el.text or "")
