"""Generated from Smithy shape ``com.amazonaws.ec2#AddressTransferStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AddressTransferStatus: TypeAlias = Literal[
    "pending",
    "disabled",
    "accepted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "disabled",
        "accepted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "disabled",
        "accepted",
    )
)


def to_ec2_query_text(value: AddressTransferStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> AddressTransferStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AddressTransferStatus value: {text!r}")
    return cast(AddressTransferStatus, text)


def serialize_ec2_query(
    value: AddressTransferStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AddressTransferStatus:
    return from_ec2_query_text(el.text or "")
