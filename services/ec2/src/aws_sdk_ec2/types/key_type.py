"""Generated from Smithy shape ``com.amazonaws.ec2#KeyType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

KeyType: TypeAlias = Literal[
    "rsa",
    "ed25519",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "rsa",
        "ed25519",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "rsa",
        "ed25519",
    )
)


def to_ec2_query_text(value: KeyType) -> str:
    return value


def from_ec2_query_text(text: str) -> KeyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown KeyType value: {text!r}")
    return cast(KeyType, text)


def serialize_ec2_query(
    value: KeyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> KeyType:
    return from_ec2_query_text(el.text or "")
