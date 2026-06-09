"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOverlapStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamOverlapStatus: TypeAlias = Literal[
    "overlapping",
    "nonoverlapping",
    "ignored",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "overlapping",
        "nonoverlapping",
        "ignored",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "overlapping",
        "nonoverlapping",
        "ignored",
    )
)


def to_ec2_query_text(value: IpamOverlapStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamOverlapStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamOverlapStatus value: {text!r}")
    return cast(IpamOverlapStatus, text)


def serialize_ec2_query(
    value: IpamOverlapStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamOverlapStatus:
    return from_ec2_query_text(el.text or "")
