"""Generated from Smithy shape ``com.amazonaws.rds#ReplicaMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

ReplicaMode: TypeAlias = Literal[
    "open-read-only",
    "mounted",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "open-read-only",
        "mounted",
    )
)


def to_query_text(value: ReplicaMode) -> str:
    return value


def from_query_text(text: str) -> ReplicaMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReplicaMode value: {text!r}")
    return cast(ReplicaMode, text)


def serialize_query(
    value: ReplicaMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReplicaMode:
    return from_query_text(el.text or "")
