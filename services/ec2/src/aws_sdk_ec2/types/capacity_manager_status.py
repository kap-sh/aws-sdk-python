"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

CapacityManagerStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityManagerStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityManagerStatus:
    return cast(CapacityManagerStatus, text)


def serialize_ec2_query(
    value: CapacityManagerStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityManagerStatus:
    return from_ec2_query_text(el.text or "")
