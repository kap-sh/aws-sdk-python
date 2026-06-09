"""Generated from Smithy shape ``com.amazonaws.ec2#ExportEnvironment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ExportEnvironment: TypeAlias = Literal[
    "citrix",
    "vmware",
    "microsoft",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "citrix",
        "vmware",
        "microsoft",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "citrix",
        "vmware",
        "microsoft",
    )
)


def to_ec2_query_text(value: ExportEnvironment) -> str:
    return value


def from_ec2_query_text(text: str) -> ExportEnvironment:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ExportEnvironment value: {text!r}")
    return cast(ExportEnvironment, text)


def serialize_ec2_query(
    value: ExportEnvironment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ExportEnvironment:
    return from_ec2_query_text(el.text or "")
