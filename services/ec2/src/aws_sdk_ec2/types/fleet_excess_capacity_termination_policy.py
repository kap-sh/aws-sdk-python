"""Generated from Smithy shape ``com.amazonaws.ec2#FleetExcessCapacityTerminationPolicy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

FleetExcessCapacityTerminationPolicy: TypeAlias = Literal[
    "no-termination",
    "termination",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "no-termination",
        "termination",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "no-termination",
        "termination",
    )
)


def to_ec2_query_text(value: FleetExcessCapacityTerminationPolicy) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetExcessCapacityTerminationPolicy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown FleetExcessCapacityTerminationPolicy value: {text!r}"
        )
    return cast(FleetExcessCapacityTerminationPolicy, text)


def serialize_ec2_query(
    value: FleetExcessCapacityTerminationPolicy,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetExcessCapacityTerminationPolicy:
    return from_ec2_query_text(el.text or "")
