"""Generated from Smithy shape ``com.amazonaws.ec2#NestedVirtualizationSpecification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

NestedVirtualizationSpecification: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def to_ec2_query_text(value: NestedVirtualizationSpecification) -> str:
    return value


def from_ec2_query_text(text: str) -> NestedVirtualizationSpecification:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown NestedVirtualizationSpecification value: {text!r}"
        )
    return cast(NestedVirtualizationSpecification, text)


def serialize_ec2_query(
    value: NestedVirtualizationSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NestedVirtualizationSpecification:
    return from_ec2_query_text(el.text or "")
