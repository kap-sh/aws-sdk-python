"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataTagsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InstanceMetadataTagsState: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceMetadataTagsState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceMetadataTagsState:
    return cast(InstanceMetadataTagsState, text)


def serialize_ec2_query(
    value: InstanceMetadataTagsState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceMetadataTagsState:
    return from_ec2_query_text(el.text or "")
