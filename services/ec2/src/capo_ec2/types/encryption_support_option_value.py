"""Generated from Smithy shape ``com.amazonaws.ec2#EncryptionSupportOptionValue``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

EncryptionSupportOptionValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EncryptionSupportOptionValue) -> str:
    return value


def from_ec2_query_text(text: str) -> EncryptionSupportOptionValue:
    return cast(EncryptionSupportOptionValue, text)


def serialize_ec2_query(
    value: EncryptionSupportOptionValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EncryptionSupportOptionValue:
    return from_ec2_query_text(el.text or "")
