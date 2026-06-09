"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneOptInStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AvailabilityZoneOptInStatus: TypeAlias = Literal[
    "opt-in-not-required",
    "opted-in",
    "not-opted-in",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "opt-in-not-required",
        "opted-in",
        "not-opted-in",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "opt-in-not-required",
        "opted-in",
        "not-opted-in",
    )
)


def to_ec2_query_text(value: AvailabilityZoneOptInStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> AvailabilityZoneOptInStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown AvailabilityZoneOptInStatus value: {text!r}"
        )
    return cast(AvailabilityZoneOptInStatus, text)


def serialize_ec2_query(
    value: AvailabilityZoneOptInStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AvailabilityZoneOptInStatus:
    return from_ec2_query_text(el.text or "")
