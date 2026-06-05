"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityTenancy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

CapacityTenancy: TypeAlias = Literal[
    "default",
    "dedicated",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "dedicated",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "dedicated",
    )
)


def to_ec2_query_text(value: CapacityTenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityTenancy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CapacityTenancy value: {text!r}")
    return cast(CapacityTenancy, text)


def serialize_ec2_query(
    value: CapacityTenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityTenancy:
    return from_ec2_query_text(el.text or "")
