"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

AccountAttributeName: TypeAlias = Literal[
    "supported-platforms",
    "default-vpc",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "supported-platforms",
        "default-vpc",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "supported-platforms",
        "default-vpc",
    )
)


def to_ec2_query_text(value: AccountAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> AccountAttributeName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AccountAttributeName value: {text!r}")
    return cast(AccountAttributeName, text)


def serialize_ec2_query(
    value: AccountAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AccountAttributeName:
    return from_ec2_query_text(el.text or "")
