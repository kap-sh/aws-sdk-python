"""Generated from Smithy shape ``com.amazonaws.ec2#PeriodType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

PeriodType: TypeAlias = Literal[
    "five-minutes",
    "fifteen-minutes",
    "one-hour",
    "three-hours",
    "one-day",
    "one-week",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "five-minutes",
        "fifteen-minutes",
        "one-hour",
        "three-hours",
        "one-day",
        "one-week",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "five-minutes",
        "fifteen-minutes",
        "one-hour",
        "three-hours",
        "one-day",
        "one-week",
    )
)


def to_ec2_query_text(value: PeriodType) -> str:
    return value


def from_ec2_query_text(text: str) -> PeriodType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PeriodType value: {text!r}")
    return cast(PeriodType, text)


def serialize_ec2_query(
    value: PeriodType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PeriodType:
    return from_ec2_query_text(el.text or "")
