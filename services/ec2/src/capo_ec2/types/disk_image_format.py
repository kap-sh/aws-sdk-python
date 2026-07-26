"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageFormat``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

DiskImageFormat: TypeAlias = Literal[
    "VMDK",
    "RAW",
    "VHD",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: DiskImageFormat) -> str:
    return value


def from_ec2_query_text(text: str) -> DiskImageFormat:
    return cast(DiskImageFormat, text)


def serialize_ec2_query(
    value: DiskImageFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DiskImageFormat:
    return from_ec2_query_text(el.text or "")
