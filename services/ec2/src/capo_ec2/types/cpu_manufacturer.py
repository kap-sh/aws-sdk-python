"""Generated from Smithy shape ``com.amazonaws.ec2#CpuManufacturer``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CpuManufacturer: TypeAlias = Literal[
    "intel",
    "amd",
    "amazon-web-services",
    "apple",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CpuManufacturer) -> str:
    return value


def from_ec2_query_text(text: str) -> CpuManufacturer:
    return cast(CpuManufacturer, text)


def serialize_ec2_query(
    value: CpuManufacturer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CpuManufacturer:
    return from_ec2_query_text(el.text or "")
