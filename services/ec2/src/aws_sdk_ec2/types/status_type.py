"""Generated from Smithy shape ``com.amazonaws.ec2#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

StatusType: TypeAlias = Literal[
    "passed",
    "failed",
    "insufficient-data",
    "initializing",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "passed",
        "failed",
        "insufficient-data",
        "initializing",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "passed",
        "failed",
        "insufficient-data",
        "initializing",
    )
)


def to_ec2_query_text(value: StatusType) -> str:
    return value


def from_ec2_query_text(text: str) -> StatusType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StatusType value: {text!r}")
    return cast(StatusType, text)


def serialize_ec2_query(
    value: StatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StatusType:
    return from_ec2_query_text(el.text or "")
