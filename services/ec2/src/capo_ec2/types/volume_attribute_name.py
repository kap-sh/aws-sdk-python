"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttributeName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

VolumeAttributeName: TypeAlias = Literal[
    "autoEnableIO",
    "productCodes",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VolumeAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeAttributeName:
    return cast(VolumeAttributeName, text)


def serialize_ec2_query(
    value: VolumeAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeAttributeName:
    return from_ec2_query_text(el.text or "")
