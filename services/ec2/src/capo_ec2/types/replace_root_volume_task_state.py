"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRootVolumeTaskState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ReplaceRootVolumeTaskState: TypeAlias = Literal[
    "pending",
    "in-progress",
    "failing",
    "succeeded",
    "failed",
    "failed-detached",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ReplaceRootVolumeTaskState) -> str:
    return value


def from_ec2_query_text(text: str) -> ReplaceRootVolumeTaskState:
    return cast(ReplaceRootVolumeTaskState, text)


def serialize_ec2_query(
    value: ReplaceRootVolumeTaskState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReplaceRootVolumeTaskState:
    return from_ec2_query_text(el.text or "")
