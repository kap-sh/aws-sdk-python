"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAttributeName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ImageAttributeName: TypeAlias = Literal[
    "description",
    "kernel",
    "ramdisk",
    "launchPermission",
    "productCodes",
    "blockDeviceMapping",
    "sriovNetSupport",
    "bootMode",
    "tpmSupport",
    "uefiData",
    "lastLaunchedTime",
    "imdsSupport",
    "deregistrationProtection",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ImageAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageAttributeName:
    return cast(ImageAttributeName, text)


def serialize_ec2_query(
    value: ImageAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageAttributeName:
    return from_ec2_query_text(el.text or "")
