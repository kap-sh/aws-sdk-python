"""Generated from Smithy shape ``com.amazonaws.ec2#FleetStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

FleetStateCode: TypeAlias = Literal[
    "submitted",
    "active",
    "deleted",
    "failed",
    "deleted_running",
    "deleted_terminating",
    "modifying",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "submitted",
        "active",
        "deleted",
        "failed",
        "deleted_running",
        "deleted_terminating",
        "modifying",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "submitted",
        "active",
        "deleted",
        "failed",
        "deleted_running",
        "deleted_terminating",
        "modifying",
    )
)


def to_ec2_query_text(value: FleetStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetStateCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FleetStateCode value: {text!r}")
    return cast(FleetStateCode, text)


def serialize_ec2_query(
    value: FleetStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetStateCode:
    return from_ec2_query_text(el.text or "")
