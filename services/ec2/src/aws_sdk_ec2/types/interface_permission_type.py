"""Generated from Smithy shape ``com.amazonaws.ec2#InterfacePermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

InterfacePermissionType: TypeAlias = Literal[
    "INSTANCE-ATTACH",
    "EIP-ASSOCIATE",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE-ATTACH",
        "EIP-ASSOCIATE",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE-ATTACH",
        "EIP-ASSOCIATE",
    )
)


def to_ec2_query_text(value: InterfacePermissionType) -> str:
    return value


def from_ec2_query_text(text: str) -> InterfacePermissionType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InterfacePermissionType value: {text!r}")
    return cast(InterfacePermissionType, text)


def serialize_ec2_query(
    value: InterfacePermissionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InterfacePermissionType:
    return from_ec2_query_text(el.text or "")
