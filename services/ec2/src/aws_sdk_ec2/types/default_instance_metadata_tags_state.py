"""Generated from Smithy shape ``com.amazonaws.ec2#DefaultInstanceMetadataTagsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

DefaultInstanceMetadataTagsState: TypeAlias = Literal[
    "disabled",
    "enabled",
    "no-preference",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: DefaultInstanceMetadataTagsState) -> str:
    return value


def from_ec2_query_text(text: str) -> DefaultInstanceMetadataTagsState:
    return cast(DefaultInstanceMetadataTagsState, text)


def serialize_ec2_query(
    value: DefaultInstanceMetadataTagsState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DefaultInstanceMetadataTagsState:
    return from_ec2_query_text(el.text or "")
