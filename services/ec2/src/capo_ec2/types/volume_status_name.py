"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

VolumeStatusName: TypeAlias = Literal[
    "io-enabled",
    "io-performance",
    "initialization-state",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VolumeStatusName) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeStatusName:
    return cast(VolumeStatusName, text)


def serialize_ec2_query(
    value: VolumeStatusName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeStatusName:
    return from_ec2_query_text(el.text or "")
