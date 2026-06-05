"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyManagedBy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamPolicyManagedBy: TypeAlias = Literal[
    "account",
    "delegated-administrator-for-ipam",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "account",
        "delegated-administrator-for-ipam",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "account",
        "delegated-administrator-for-ipam",
    )
)


def to_ec2_query_text(value: IpamPolicyManagedBy) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPolicyManagedBy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamPolicyManagedBy value: {text!r}")
    return cast(IpamPolicyManagedBy, text)


def serialize_ec2_query(
    value: IpamPolicyManagedBy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPolicyManagedBy:
    return from_ec2_query_text(el.text or "")
