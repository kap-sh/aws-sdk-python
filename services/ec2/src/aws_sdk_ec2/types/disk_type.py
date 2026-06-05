"""Generated from Smithy shape ``com.amazonaws.ec2#DiskType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

DiskType: TypeAlias = Literal[
    "hdd",
    "ssd",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "hdd",
        "ssd",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "hdd",
        "ssd",
    )
)


def to_ec2_query_text(value: DiskType) -> str:
    return value


def from_ec2_query_text(text: str) -> DiskType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DiskType value: {text!r}")
    return cast(DiskType, text)


def serialize_ec2_query(
    value: DiskType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DiskType:
    return from_ec2_query_text(el.text or "")
