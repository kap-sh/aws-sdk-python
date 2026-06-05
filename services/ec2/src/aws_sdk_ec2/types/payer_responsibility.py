"""Generated from Smithy shape ``com.amazonaws.ec2#PayerResponsibility``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

PayerResponsibility: TypeAlias = Literal["ServiceOwner",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("ServiceOwner",))


_VALUES: frozenset[str] = frozenset(("ServiceOwner",))


def to_ec2_query_text(value: PayerResponsibility) -> str:
    return value


def from_ec2_query_text(text: str) -> PayerResponsibility:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PayerResponsibility value: {text!r}")
    return cast(PayerResponsibility, text)


def serialize_ec2_query(
    value: PayerResponsibility, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PayerResponsibility:
    return from_ec2_query_text(el.text or "")
