"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AvailabilityMode: TypeAlias = Literal[
    "zonal",
    "regional",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AvailabilityMode) -> str:
    return value


def from_ec2_query_text(text: str) -> AvailabilityMode:
    return cast(AvailabilityMode, text)


def serialize_ec2_query(
    value: AvailabilityMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AvailabilityMode:
    return from_ec2_query_text(el.text or "")
