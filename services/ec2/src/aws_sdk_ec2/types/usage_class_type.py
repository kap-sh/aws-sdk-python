"""Generated from Smithy shape ``com.amazonaws.ec2#UsageClassType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

UsageClassType: TypeAlias = Literal[
    "spot",
    "on-demand",
    "capacity-block",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "on-demand",
        "capacity-block",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "on-demand",
        "capacity-block",
    )
)


def to_ec2_query_text(value: UsageClassType) -> str:
    return value


def from_ec2_query_text(text: str) -> UsageClassType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown UsageClassType value: {text!r}")
    return cast(UsageClassType, text)


def serialize_ec2_query(
    value: UsageClassType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> UsageClassType:
    return from_ec2_query_text(el.text or "")
