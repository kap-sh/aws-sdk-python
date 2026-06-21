"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlExclusionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

VpcEncryptionControlExclusionState: TypeAlias = Literal[
    "enabling",
    "enabled",
    "disabling",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VpcEncryptionControlExclusionState) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcEncryptionControlExclusionState:
    return cast(VpcEncryptionControlExclusionState, text)


def serialize_ec2_query(
    value: VpcEncryptionControlExclusionState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlExclusionState:
    return from_ec2_query_text(el.text or "")
