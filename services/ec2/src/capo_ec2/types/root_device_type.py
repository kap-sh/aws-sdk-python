"""Generated from Smithy shape ``com.amazonaws.ec2#RootDeviceType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

RootDeviceType: TypeAlias = Literal[
    "ebs",
    "instance-store",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RootDeviceType) -> str:
    return value


def from_ec2_query_text(text: str) -> RootDeviceType:
    return cast(RootDeviceType, text)


def serialize_ec2_query(
    value: RootDeviceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RootDeviceType:
    return from_ec2_query_text(el.text or "")
