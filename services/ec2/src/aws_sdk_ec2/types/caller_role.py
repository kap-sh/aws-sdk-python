"""Generated from Smithy shape ``com.amazonaws.ec2#CallerRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

CallerRole: TypeAlias = Literal[
    "odcr-owner",
    "unused-reservation-billing-owner",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CallerRole) -> str:
    return value


def from_ec2_query_text(text: str) -> CallerRole:
    return cast(CallerRole, text)


def serialize_ec2_query(
    value: CallerRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CallerRole:
    return from_ec2_query_text(el.text or "")
