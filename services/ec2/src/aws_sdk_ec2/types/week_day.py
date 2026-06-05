"""Generated from Smithy shape ``com.amazonaws.ec2#WeekDay``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

WeekDay: TypeAlias = Literal[
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    )
)


def to_ec2_query_text(value: WeekDay) -> str:
    return value


def from_ec2_query_text(text: str) -> WeekDay:
    if text not in _VALUES:
        raise DeserializationError(f"unknown WeekDay value: {text!r}")
    return cast(WeekDay, text)


def serialize_ec2_query(
    value: WeekDay, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> WeekDay:
    return from_ec2_query_text(el.text or "")
