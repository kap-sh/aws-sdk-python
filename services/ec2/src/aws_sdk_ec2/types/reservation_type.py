"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ReservationType: TypeAlias = Literal[
    "capacity-block",
    "odcr",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "capacity-block",
        "odcr",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "capacity-block",
        "odcr",
    )
)


def to_ec2_query_text(value: ReservationType) -> str:
    return value


def from_ec2_query_text(text: str) -> ReservationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReservationType value: {text!r}")
    return cast(ReservationType, text)


def serialize_ec2_query(
    value: ReservationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReservationType:
    return from_ec2_query_text(el.text or "")
