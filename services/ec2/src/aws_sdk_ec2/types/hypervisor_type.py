"""Generated from Smithy shape ``com.amazonaws.ec2#HypervisorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

HypervisorType: TypeAlias = Literal[
    "ovm",
    "xen",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: HypervisorType) -> str:
    return value


def from_ec2_query_text(text: str) -> HypervisorType:
    return cast(HypervisorType, text)


def serialize_ec2_query(
    value: HypervisorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HypervisorType:
    return from_ec2_query_text(el.text or "")
