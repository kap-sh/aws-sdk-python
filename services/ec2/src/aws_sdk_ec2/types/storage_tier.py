"""Generated from Smithy shape ``com.amazonaws.ec2#StorageTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

StorageTier: TypeAlias = Literal[
    "archive",
    "standard",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "archive",
        "standard",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "archive",
        "standard",
    )
)


def to_ec2_query_text(value: StorageTier) -> str:
    return value


def from_ec2_query_text(text: str) -> StorageTier:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StorageTier value: {text!r}")
    return cast(StorageTier, text)


def serialize_ec2_query(
    value: StorageTier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StorageTier:
    return from_ec2_query_text(el.text or "")
