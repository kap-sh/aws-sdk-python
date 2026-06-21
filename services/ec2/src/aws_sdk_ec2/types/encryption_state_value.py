"""Generated from Smithy shape ``com.amazonaws.ec2#EncryptionStateValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

EncryptionStateValue: TypeAlias = Literal[
    "enabling",
    "enabled",
    "disabling",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EncryptionStateValue) -> str:
    return value


def from_ec2_query_text(text: str) -> EncryptionStateValue:
    return cast(EncryptionStateValue, text)


def serialize_ec2_query(
    value: EncryptionStateValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EncryptionStateValue:
    return from_ec2_query_text(el.text or "")
