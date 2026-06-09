"""Generated from Smithy shape ``com.amazonaws.ec2#HostnameType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

HostnameType: TypeAlias = Literal[
    "ip-name",
    "resource-name",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ip-name",
        "resource-name",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ip-name",
        "resource-name",
    )
)


def to_ec2_query_text(value: HostnameType) -> str:
    return value


def from_ec2_query_text(text: str) -> HostnameType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HostnameType value: {text!r}")
    return cast(HostnameType, text)


def serialize_ec2_query(
    value: HostnameType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HostnameType:
    return from_ec2_query_text(el.text or "")
