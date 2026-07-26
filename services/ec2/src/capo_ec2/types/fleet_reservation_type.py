"""Generated from Smithy shape ``com.amazonaws.ec2#FleetReservationType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FleetReservationType: TypeAlias = Literal["interruptible-capacity-reservation",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetReservationType) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetReservationType:
    return cast(FleetReservationType, text)


def serialize_ec2_query(
    value: FleetReservationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetReservationType:
    return from_ec2_query_text(el.text or "")
