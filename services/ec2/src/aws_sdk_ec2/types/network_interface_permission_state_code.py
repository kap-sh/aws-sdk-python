"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermissionStateCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

NetworkInterfacePermissionStateCode: TypeAlias = Literal[
    "pending",
    "granted",
    "revoking",
    "revoked",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "granted",
        "revoking",
        "revoked",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "granted",
        "revoking",
        "revoked",
    )
)


def to_ec2_query_text(value: NetworkInterfacePermissionStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> NetworkInterfacePermissionStateCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown NetworkInterfacePermissionStateCode value: {text!r}"
        )
    return cast(NetworkInterfacePermissionStateCode, text)


def serialize_ec2_query(
    value: NetworkInterfacePermissionStateCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NetworkInterfacePermissionStateCode:
    return from_ec2_query_text(el.text or "")
