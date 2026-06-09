"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AllocationType: TypeAlias = Literal[
    "used",
    "future",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "used",
        "future",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "used",
        "future",
    )
)


def to_ec2_query_text(value: AllocationType) -> str:
    return value


def from_ec2_query_text(text: str) -> AllocationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AllocationType value: {text!r}")
    return cast(AllocationType, text)


def serialize_ec2_query(
    value: AllocationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AllocationType:
    return from_ec2_query_text(el.text or "")
