"""Generated from Smithy shape ``com.amazonaws.ec2#MarketType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

MarketType: TypeAlias = Literal[
    "spot",
    "capacity-block",
    "interruptible-capacity-reservation",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "capacity-block",
        "interruptible-capacity-reservation",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "capacity-block",
        "interruptible-capacity-reservation",
    )
)


def to_ec2_query_text(value: MarketType) -> str:
    return value


def from_ec2_query_text(text: str) -> MarketType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MarketType value: {text!r}")
    return cast(MarketType, text)


def serialize_ec2_query(
    value: MarketType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MarketType:
    return from_ec2_query_text(el.text or "")
