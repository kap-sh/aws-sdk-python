"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataEndpointState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceMetadataEndpointState: TypeAlias = Literal[
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


def to_ec2_query_text(value: InstanceMetadataEndpointState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceMetadataEndpointState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceMetadataEndpointState value: {text!r}"
        )
    return cast(InstanceMetadataEndpointState, text)


def serialize_ec2_query(
    value: InstanceMetadataEndpointState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceMetadataEndpointState:
    return from_ec2_query_text(el.text or "")
