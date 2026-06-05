"""Generated from Smithy shape ``com.amazonaws.ec2#IpamComplianceStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamComplianceStatus: TypeAlias = Literal[
    "compliant",
    "noncompliant",
    "unmanaged",
    "ignored",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "compliant",
        "noncompliant",
        "unmanaged",
        "ignored",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "compliant",
        "noncompliant",
        "unmanaged",
        "ignored",
    )
)


def to_ec2_query_text(value: IpamComplianceStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamComplianceStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamComplianceStatus value: {text!r}")
    return cast(IpamComplianceStatus, text)


def serialize_ec2_query(
    value: IpamComplianceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamComplianceStatus:
    return from_ec2_query_text(el.text or "")
