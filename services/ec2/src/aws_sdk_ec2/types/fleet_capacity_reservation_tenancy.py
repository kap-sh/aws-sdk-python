"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservationTenancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

FleetCapacityReservationTenancy: TypeAlias = Literal["default",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("default",))


_VALUES: frozenset[str] = frozenset(("default",))


def to_ec2_query_text(value: FleetCapacityReservationTenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetCapacityReservationTenancy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown FleetCapacityReservationTenancy value: {text!r}"
        )
    return cast(FleetCapacityReservationTenancy, text)


def serialize_ec2_query(
    value: FleetCapacityReservationTenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetCapacityReservationTenancy:
    return from_ec2_query_text(el.text or "")
