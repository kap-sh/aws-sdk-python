"""Generated from Smithy shape ``com.amazonaws.ec2#ProductCodeValues``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ProductCodeValues: TypeAlias = Literal[
    "devpay",
    "marketplace",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "devpay",
        "marketplace",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "devpay",
        "marketplace",
    )
)


def to_ec2_query_text(value: ProductCodeValues) -> str:
    return value


def from_ec2_query_text(text: str) -> ProductCodeValues:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ProductCodeValues value: {text!r}")
    return cast(ProductCodeValues, text)


def serialize_ec2_query(
    value: ProductCodeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ProductCodeValues:
    return from_ec2_query_text(el.text or "")
