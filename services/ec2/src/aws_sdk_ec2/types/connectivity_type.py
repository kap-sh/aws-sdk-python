"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectivityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ConnectivityType: TypeAlias = Literal[
    "private",
    "public",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "private",
        "public",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "private",
        "public",
    )
)


def to_ec2_query_text(value: ConnectivityType) -> str:
    return value


def from_ec2_query_text(text: str) -> ConnectivityType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ConnectivityType value: {text!r}")
    return cast(ConnectivityType, text)


def serialize_ec2_query(
    value: ConnectivityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ConnectivityType:
    return from_ec2_query_text(el.text or "")
