"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttributeName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VolumeAttributeName: TypeAlias = Literal[
    "autoEnableIO",
    "productCodes",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "autoEnableIO",
        "productCodes",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "autoEnableIO",
        "productCodes",
    )
)


def to_ec2_query_text(value: VolumeAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeAttributeName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VolumeAttributeName value: {text!r}")
    return cast(VolumeAttributeName, text)


def serialize_ec2_query(
    value: VolumeAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeAttributeName:
    return from_ec2_query_text(el.text or "")
