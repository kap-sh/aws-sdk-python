"""Generated from Smithy shape ``com.amazonaws.ec2#FleetReservationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

FleetReservationType: TypeAlias = Literal["interruptible-capacity-reservation",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("interruptible-capacity-reservation",))


_VALUES: frozenset[str] = frozenset(("interruptible-capacity-reservation",))


def to_ec2_query_text(value: FleetReservationType) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetReservationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FleetReservationType value: {text!r}")
    return cast(FleetReservationType, text)


def serialize_ec2_query(
    value: FleetReservationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetReservationType:
    return from_ec2_query_text(el.text or "")
