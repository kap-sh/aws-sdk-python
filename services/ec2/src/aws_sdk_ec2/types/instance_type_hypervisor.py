"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeHypervisor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InstanceTypeHypervisor: TypeAlias = Literal[
    "nitro",
    "xen",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceTypeHypervisor) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceTypeHypervisor:
    return cast(InstanceTypeHypervisor, text)


def serialize_ec2_query(
    value: InstanceTypeHypervisor, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceTypeHypervisor:
    return from_ec2_query_text(el.text or "")
