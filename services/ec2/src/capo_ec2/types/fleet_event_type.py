"""Generated from Smithy shape ``com.amazonaws.ec2#FleetEventType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FleetEventType: TypeAlias = Literal[
    "instance-change",
    "fleet-change",
    "service-error",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetEventType) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetEventType:
    return cast(FleetEventType, text)


def serialize_ec2_query(
    value: FleetEventType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetEventType:
    return from_ec2_query_text(el.text or "")
