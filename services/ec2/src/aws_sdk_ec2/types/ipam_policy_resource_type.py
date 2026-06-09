"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamPolicyResourceType: TypeAlias = Literal[
    "alb",
    "eip",
    "rds",
    "rnat",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "alb",
        "eip",
        "rds",
        "rnat",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "alb",
        "eip",
        "rds",
        "rnat",
    )
)


def to_ec2_query_text(value: IpamPolicyResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPolicyResourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamPolicyResourceType value: {text!r}")
    return cast(IpamPolicyResourceType, text)


def serialize_ec2_query(
    value: IpamPolicyResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPolicyResourceType:
    return from_ec2_query_text(el.text or "")
