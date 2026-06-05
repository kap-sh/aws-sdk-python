"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataOptionsState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceMetadataOptionsState: TypeAlias = Literal[
    "pending",
    "applied",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "applied",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "applied",
    )
)


def to_ec2_query_text(value: InstanceMetadataOptionsState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceMetadataOptionsState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceMetadataOptionsState value: {text!r}"
        )
    return cast(InstanceMetadataOptionsState, text)


def serialize_ec2_query(
    value: InstanceMetadataOptionsState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceMetadataOptionsState:
    return from_ec2_query_text(el.text or "")
