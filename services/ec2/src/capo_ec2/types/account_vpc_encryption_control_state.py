"""Generated from Smithy shape ``com.amazonaws.ec2#AccountVpcEncryptionControlState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AccountVpcEncryptionControlState: TypeAlias = Literal[
    "default-state",
    "transitions-in-progress",
    "transitions-partially-successful",
    "transitions-successful",
    "transitions-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AccountVpcEncryptionControlState) -> str:
    return value


def from_ec2_query_text(text: str) -> AccountVpcEncryptionControlState:
    return cast(AccountVpcEncryptionControlState, text)


def serialize_ec2_query(
    value: AccountVpcEncryptionControlState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AccountVpcEncryptionControlState:
    return from_ec2_query_text(el.text or "")
