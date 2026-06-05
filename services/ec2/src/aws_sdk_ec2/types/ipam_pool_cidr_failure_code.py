"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrFailureCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamPoolCidrFailureCode: TypeAlias = Literal[
    "cidr-not-available",
    "limit-exceeded",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cidr-not-available",
        "limit-exceeded",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "cidr-not-available",
        "limit-exceeded",
    )
)


def to_ec2_query_text(value: IpamPoolCidrFailureCode) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPoolCidrFailureCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamPoolCidrFailureCode value: {text!r}")
    return cast(IpamPoolCidrFailureCode, text)


def serialize_ec2_query(
    value: IpamPoolCidrFailureCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPoolCidrFailureCode:
    return from_ec2_query_text(el.text or "")
