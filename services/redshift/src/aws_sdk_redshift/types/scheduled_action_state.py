"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ScheduledActionState: TypeAlias = Literal[
    "ACTIVE",
    "DISABLED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DISABLED",
    )
)


def to_query_text(value: ScheduledActionState) -> str:
    return value


def from_query_text(text: str) -> ScheduledActionState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScheduledActionState value: {text!r}")
    return cast(ScheduledActionState, text)


def serialize_query(
    value: ScheduledActionState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduledActionState:
    return from_query_text(el.text or "")
