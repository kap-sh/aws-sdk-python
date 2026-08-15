"""Generated from Smithy shape ``com.amazonaws.ec2#TaggableResourceType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TaggableResourceType: TypeAlias = Literal[
    "network-interface",
    "instance",
    "auto-scaling-group",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TaggableResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> TaggableResourceType:
    return cast(TaggableResourceType, text)


def serialize_ec2_query(
    value: TaggableResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TaggableResourceType:
    return from_ec2_query_text(el.text or "")
