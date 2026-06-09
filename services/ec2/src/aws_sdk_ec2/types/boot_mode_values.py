"""Generated from Smithy shape ``com.amazonaws.ec2#BootModeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

BootModeValues: TypeAlias = Literal[
    "legacy-bios",
    "uefi",
    "uefi-preferred",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "legacy-bios",
        "uefi",
        "uefi-preferred",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "legacy-bios",
        "uefi",
        "uefi-preferred",
    )
)


def to_ec2_query_text(value: BootModeValues) -> str:
    return value


def from_ec2_query_text(text: str) -> BootModeValues:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BootModeValues value: {text!r}")
    return cast(BootModeValues, text)


def serialize_ec2_query(
    value: BootModeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BootModeValues:
    return from_ec2_query_text(el.text or "")
