"""Generated from Smithy shape ``com.amazonaws.ec2#RootDeviceType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

RootDeviceType: TypeAlias = Literal[
    "ebs",
    "instance-store",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ebs",
        "instance-store",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ebs",
        "instance-store",
    )
)


def to_ec2_query_text(value: RootDeviceType) -> str:
    return value


def from_ec2_query_text(text: str) -> RootDeviceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RootDeviceType value: {text!r}")
    return cast(RootDeviceType, text)


def serialize_ec2_query(
    value: RootDeviceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RootDeviceType:
    return from_ec2_query_text(el.text or "")
