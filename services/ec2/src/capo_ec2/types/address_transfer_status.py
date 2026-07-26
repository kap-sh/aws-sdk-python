"""Generated from Smithy shape ``com.amazonaws.ec2#AddressTransferStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AddressTransferStatus: TypeAlias = Literal[
    "pending",
    "disabled",
    "accepted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AddressTransferStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> AddressTransferStatus:
    return cast(AddressTransferStatus, text)


def serialize_ec2_query(
    value: AddressTransferStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AddressTransferStatus:
    return from_ec2_query_text(el.text or "")
