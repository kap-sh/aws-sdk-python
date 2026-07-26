"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationEndDateType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ReservationEndDateType: TypeAlias = Literal[
    "limited",
    "unlimited",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ReservationEndDateType) -> str:
    return value


def from_ec2_query_text(text: str) -> ReservationEndDateType:
    return cast(ReservationEndDateType, text)


def serialize_ec2_query(
    value: ReservationEndDateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReservationEndDateType:
    return from_ec2_query_text(el.text or "")
