"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataOptionsState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InstanceMetadataOptionsState: TypeAlias = Literal[
    "pending",
    "applied",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceMetadataOptionsState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceMetadataOptionsState:
    return cast(InstanceMetadataOptionsState, text)


def serialize_ec2_query(
    value: InstanceMetadataOptionsState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceMetadataOptionsState:
    return from_ec2_query_text(el.text or "")
