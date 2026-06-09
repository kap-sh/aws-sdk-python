"""Generated from Smithy shape ``com.amazonaws.ec2#LocalStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LocalStorageType: TypeAlias = Literal[
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


def to_ec2_query_text(value: LocalStorageType) -> str:
    return value


def from_ec2_query_text(text: str) -> LocalStorageType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LocalStorageType value: {text!r}")
    return cast(LocalStorageType, text)


def serialize_ec2_query(
    value: LocalStorageType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LocalStorageType:
    return from_ec2_query_text(el.text or "")
