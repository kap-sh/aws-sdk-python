"""Generated from Smithy shape ``com.amazonaws.ec2#PrincipalType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

PrincipalType: TypeAlias = Literal[
    "All",
    "Service",
    "OrganizationUnit",
    "Account",
    "User",
    "Role",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Service",
        "OrganizationUnit",
        "Account",
        "User",
        "Role",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Service",
        "OrganizationUnit",
        "Account",
        "User",
        "Role",
    )
)


def to_ec2_query_text(value: PrincipalType) -> str:
    return value


def from_ec2_query_text(text: str) -> PrincipalType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PrincipalType value: {text!r}")
    return cast(PrincipalType, text)


def serialize_ec2_query(
    value: PrincipalType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PrincipalType:
    return from_ec2_query_text(el.text or "")
