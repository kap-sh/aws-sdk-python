"""Generated from Smithy shape ``com.amazonaws.ec2#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "add",
    "remove",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "add",
        "remove",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "add",
        "remove",
    )
)


def to_ec2_query_text(value: OperationType) -> str:
    return value


def from_ec2_query_text(text: str) -> OperationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {text!r}")
    return cast(OperationType, text)


def serialize_ec2_query(
    value: OperationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OperationType:
    return from_ec2_query_text(el.text or "")
