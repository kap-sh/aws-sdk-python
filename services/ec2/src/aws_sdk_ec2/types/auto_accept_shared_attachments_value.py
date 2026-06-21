"""Generated from Smithy shape ``com.amazonaws.ec2#AutoAcceptSharedAttachmentsValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AutoAcceptSharedAttachmentsValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AutoAcceptSharedAttachmentsValue) -> str:
    return value


def from_ec2_query_text(text: str) -> AutoAcceptSharedAttachmentsValue:
    return cast(AutoAcceptSharedAttachmentsValue, text)


def serialize_ec2_query(
    value: AutoAcceptSharedAttachmentsValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AutoAcceptSharedAttachmentsValue:
    return from_ec2_query_text(el.text or "")
