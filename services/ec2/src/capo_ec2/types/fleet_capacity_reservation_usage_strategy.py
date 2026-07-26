"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservationUsageStrategy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FleetCapacityReservationUsageStrategy: TypeAlias = Literal[
    "use-capacity-reservations-first",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetCapacityReservationUsageStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetCapacityReservationUsageStrategy:
    return cast(FleetCapacityReservationUsageStrategy, text)


def serialize_ec2_query(
    value: FleetCapacityReservationUsageStrategy,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetCapacityReservationUsageStrategy:
    return from_ec2_query_text(el.text or "")
