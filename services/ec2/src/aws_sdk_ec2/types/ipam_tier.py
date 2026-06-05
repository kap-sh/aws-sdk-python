"""Generated from Smithy shape ``com.amazonaws.ec2#IpamTier``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpamTier: TypeAlias = Literal[
    "free",
    "advanced",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "free",
        "advanced",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "free",
        "advanced",
    )
)


def to_ec2_query_text(value: IpamTier) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamTier:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamTier value: {text!r}")
    return cast(IpamTier, text)


def serialize_ec2_query(
    value: IpamTier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamTier:
    return from_ec2_query_text(el.text or "")
