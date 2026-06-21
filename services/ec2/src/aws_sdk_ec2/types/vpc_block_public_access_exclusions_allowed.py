"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusionsAllowed``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

VpcBlockPublicAccessExclusionsAllowed: TypeAlias = Literal[
    "allowed",
    "not-allowed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VpcBlockPublicAccessExclusionsAllowed) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcBlockPublicAccessExclusionsAllowed:
    return cast(VpcBlockPublicAccessExclusionsAllowed, text)


def serialize_ec2_query(
    value: VpcBlockPublicAccessExclusionsAllowed,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcBlockPublicAccessExclusionsAllowed:
    return from_ec2_query_text(el.text or "")
