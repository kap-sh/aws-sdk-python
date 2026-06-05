"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataProtocolState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceMetadataProtocolState: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


def to_ec2_query_text(value: InstanceMetadataProtocolState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceMetadataProtocolState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceMetadataProtocolState value: {text!r}"
        )
    return cast(InstanceMetadataProtocolState, text)


def serialize_ec2_query(
    value: InstanceMetadataProtocolState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceMetadataProtocolState:
    return from_ec2_query_text(el.text or "")
