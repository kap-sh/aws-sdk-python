"""Generated from Smithy shape ``com.amazonaws.ec2#BgpStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

BgpStatus: TypeAlias = Literal[
    "up",
    "down",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "up",
        "down",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "up",
        "down",
    )
)


def to_ec2_query_text(value: BgpStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> BgpStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BgpStatus value: {text!r}")
    return cast(BgpStatus, text)


def serialize_ec2_query(
    value: BgpStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BgpStatus:
    return from_ec2_query_text(el.text or "")
