"""Generated from Smithy shape ``com.amazonaws.ec2#DomainType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DomainType: TypeAlias = Literal[
    "vpc",
    "standard",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "vpc",
        "standard",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "vpc",
        "standard",
    )
)


def to_ec2_query_text(value: DomainType) -> str:
    return value


def from_ec2_query_text(text: str) -> DomainType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DomainType value: {text!r}")
    return cast(DomainType, text)


def serialize_ec2_query(
    value: DomainType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DomainType:
    return from_ec2_query_text(el.text or "")
