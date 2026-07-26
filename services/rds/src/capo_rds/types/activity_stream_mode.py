"""Generated from Smithy shape ``com.amazonaws.rds#ActivityStreamMode``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

ActivityStreamMode: TypeAlias = Literal[
    "sync",
    "async",
]


# --- awsQuery ser/de ---
def to_query_text(value: ActivityStreamMode) -> str:
    return value


def from_query_text(text: str) -> ActivityStreamMode:
    return cast(ActivityStreamMode, text)


def serialize_query(
    value: ActivityStreamMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActivityStreamMode:
    return from_query_text(el.text or "")
