"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceAttributeName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InstanceAttributeName: TypeAlias = Literal[
    "instanceType",
    "kernel",
    "ramdisk",
    "userData",
    "disableApiTermination",
    "instanceInitiatedShutdownBehavior",
    "rootDeviceName",
    "blockDeviceMapping",
    "productCodes",
    "sourceDestCheck",
    "groupSet",
    "ebsOptimized",
    "sriovNetSupport",
    "enaSupport",
    "enclaveOptions",
    "disableApiStop",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceAttributeName:
    return cast(InstanceAttributeName, text)


def serialize_ec2_query(
    value: InstanceAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceAttributeName:
    return from_ec2_query_text(el.text or "")
