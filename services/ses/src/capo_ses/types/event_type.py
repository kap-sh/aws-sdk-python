"""Generated from Smithy shape ``com.amazonaws.ses#EventType``."""

from typing import Literal, TypeAlias, cast

from capo_ses._protocol.xml import Element

EventType: TypeAlias = Literal[
    "send",
    "reject",
    "bounce",
    "complaint",
    "delivery",
    "open",
    "click",
    "renderingFailure",
]


# --- awsQuery ser/de ---
def to_query_text(value: EventType) -> str:
    return value


def from_query_text(text: str) -> EventType:
    return cast(EventType, text)


def serialize_query(
    value: EventType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EventType:
    return from_query_text(el.text or "")
