"""Generated from Smithy shape ``com.amazonaws.ec2#AccountVpcEncryptionControlMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AccountVpcEncryptionControlMode: TypeAlias = Literal[
    "unmanaged",
    "attempt-monitor",
    "attempt-enforce",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AccountVpcEncryptionControlMode) -> str:
    return value


def from_ec2_query_text(text: str) -> AccountVpcEncryptionControlMode:
    return cast(AccountVpcEncryptionControlMode, text)


def serialize_ec2_query(
    value: AccountVpcEncryptionControlMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AccountVpcEncryptionControlMode:
    return from_ec2_query_text(el.text or "")
