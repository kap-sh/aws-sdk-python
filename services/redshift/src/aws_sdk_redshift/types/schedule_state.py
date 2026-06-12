"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ScheduleState: TypeAlias = Literal[
    "MODIFYING",
    "ACTIVE",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODIFYING",
        "ACTIVE",
        "FAILED",
    )
)


def to_query_text(value: ScheduleState) -> str:
    return value


def from_query_text(text: str) -> ScheduleState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScheduleState value: {text!r}")
    return cast(ScheduleState, text)


def serialize_query(
    value: ScheduleState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduleState:
    return from_query_text(el.text or "")
