"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBootModeValues``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InstanceBootModeValues: TypeAlias = Literal[
    "legacy-bios",
    "uefi",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceBootModeValues) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceBootModeValues:
    return cast(InstanceBootModeValues, text)


def serialize_ec2_query(
    value: InstanceBootModeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceBootModeValues:
    return from_ec2_query_text(el.text or "")
