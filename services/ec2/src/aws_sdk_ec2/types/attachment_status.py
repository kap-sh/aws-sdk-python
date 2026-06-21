"""Generated from Smithy shape ``com.amazonaws.ec2#AttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AttachmentStatus: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AttachmentStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> AttachmentStatus:
    return cast(AttachmentStatus, text)


def serialize_ec2_query(
    value: AttachmentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AttachmentStatus:
    return from_ec2_query_text(el.text or "")
