"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeModificationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

VolumeModificationState: TypeAlias = Literal[
    "modifying",
    "optimizing",
    "completed",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VolumeModificationState) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeModificationState:
    return cast(VolumeModificationState, text)


def serialize_ec2_query(
    value: VolumeModificationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeModificationState:
    return from_ec2_query_text(el.text or "")
