"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusionState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

VpcBlockPublicAccessExclusionState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "update-in-progress",
    "update-complete",
    "update-failed",
    "delete-in-progress",
    "delete-complete",
    "disable-in-progress",
    "disable-complete",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VpcBlockPublicAccessExclusionState) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcBlockPublicAccessExclusionState:
    return cast(VpcBlockPublicAccessExclusionState, text)


def serialize_ec2_query(
    value: VpcBlockPublicAccessExclusionState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcBlockPublicAccessExclusionState:
    return from_ec2_query_text(el.text or "")
