"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAvailabilityZoneOptInStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ModifyAvailabilityZoneOptInStatus: TypeAlias = Literal[
    "opted-in",
    "not-opted-in",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ModifyAvailabilityZoneOptInStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ModifyAvailabilityZoneOptInStatus:
    return cast(ModifyAvailabilityZoneOptInStatus, text)


def serialize_ec2_query(
    value: ModifyAvailabilityZoneOptInStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ModifyAvailabilityZoneOptInStatus:
    return from_ec2_query_text(el.text or "")
