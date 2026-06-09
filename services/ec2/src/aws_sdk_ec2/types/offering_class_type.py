"""Generated from Smithy shape ``com.amazonaws.ec2#OfferingClassType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

OfferingClassType: TypeAlias = Literal[
    "standard",
    "convertible",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "convertible",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "convertible",
    )
)


def to_ec2_query_text(value: OfferingClassType) -> str:
    return value


def from_ec2_query_text(text: str) -> OfferingClassType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OfferingClassType value: {text!r}")
    return cast(OfferingClassType, text)


def serialize_ec2_query(
    value: OfferingClassType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OfferingClassType:
    return from_ec2_query_text(el.text or "")
