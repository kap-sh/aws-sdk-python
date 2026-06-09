"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

FpgaImageStateCode: TypeAlias = Literal[
    "pending",
    "failed",
    "available",
    "unavailable",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "failed",
        "available",
        "unavailable",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "failed",
        "available",
        "unavailable",
    )
)


def to_ec2_query_text(value: FpgaImageStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> FpgaImageStateCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FpgaImageStateCode value: {text!r}")
    return cast(FpgaImageStateCode, text)


def serialize_ec2_query(
    value: FpgaImageStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FpgaImageStateCode:
    return from_ec2_query_text(el.text or "")
