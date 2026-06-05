"""Generated from Smithy shape ``com.amazonaws.ec2#IpamManagementState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamManagementState: TypeAlias = Literal[
    "managed",
    "unmanaged",
    "ignored",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "managed",
        "unmanaged",
        "ignored",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "managed",
        "unmanaged",
        "ignored",
    )
)


def to_ec2_query_text(value: IpamManagementState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamManagementState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamManagementState value: {text!r}")
    return cast(IpamManagementState, text)


def serialize_ec2_query(
    value: IpamManagementState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamManagementState:
    return from_ec2_query_text(el.text or "")
