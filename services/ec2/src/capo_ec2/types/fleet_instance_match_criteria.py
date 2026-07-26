"""Generated from Smithy shape ``com.amazonaws.ec2#FleetInstanceMatchCriteria``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FleetInstanceMatchCriteria: TypeAlias = Literal["open",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FleetInstanceMatchCriteria) -> str:
    return value


def from_ec2_query_text(text: str) -> FleetInstanceMatchCriteria:
    return cast(FleetInstanceMatchCriteria, text)


def serialize_ec2_query(
    value: FleetInstanceMatchCriteria, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FleetInstanceMatchCriteria:
    return from_ec2_query_text(el.text or "")
