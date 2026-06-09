"""Generated from Smithy shape ``com.amazonaws.ec2#IpamMeteredAccount``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamMeteredAccount: TypeAlias = Literal[
    "ipam-owner",
    "resource-owner",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipam-owner",
        "resource-owner",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ipam-owner",
        "resource-owner",
    )
)


def to_ec2_query_text(value: IpamMeteredAccount) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamMeteredAccount:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamMeteredAccount value: {text!r}")
    return cast(IpamMeteredAccount, text)


def serialize_ec2_query(
    value: IpamMeteredAccount, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamMeteredAccount:
    return from_ec2_query_text(el.text or "")
