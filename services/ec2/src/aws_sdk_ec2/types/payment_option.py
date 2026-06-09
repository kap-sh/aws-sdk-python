"""Generated from Smithy shape ``com.amazonaws.ec2#PaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

PaymentOption: TypeAlias = Literal[
    "AllUpfront",
    "PartialUpfront",
    "NoUpfront",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AllUpfront",
        "PartialUpfront",
        "NoUpfront",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "AllUpfront",
        "PartialUpfront",
        "NoUpfront",
    )
)


def to_ec2_query_text(value: PaymentOption) -> str:
    return value


def from_ec2_query_text(text: str) -> PaymentOption:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PaymentOption value: {text!r}")
    return cast(PaymentOption, text)


def serialize_ec2_query(
    value: PaymentOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PaymentOption:
    return from_ec2_query_text(el.text or "")
