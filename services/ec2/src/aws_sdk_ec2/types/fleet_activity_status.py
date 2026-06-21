"""Generated from Smithy shape ``com.amazonaws.ec2#FleetActivityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

FleetActivityStatus: TypeAlias = Literal[
    "error",
    "pending_fulfillment",
    "pending_termination",
    "fulfilled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetActivityStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetActivityStatus:
    return cast(FleetActivityStatus, text)


def serialize_ec2_query(
    value: FleetActivityStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetActivityStatus:
    return from_ec2_query_text(el.text or "")
