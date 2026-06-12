"""Generated from Smithy shape ``com.amazonaws.rds#ActivityStreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

ActivityStreamStatus: TypeAlias = Literal[
    "stopped",
    "starting",
    "started",
    "stopping",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "stopped",
        "starting",
        "started",
        "stopping",
    )
)


def to_query_text(value: ActivityStreamStatus) -> str:
    return value


def from_query_text(text: str) -> ActivityStreamStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ActivityStreamStatus value: {text!r}")
    return cast(ActivityStreamStatus, text)


def serialize_query(
    value: ActivityStreamStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActivityStreamStatus:
    return from_query_text(el.text or "")
