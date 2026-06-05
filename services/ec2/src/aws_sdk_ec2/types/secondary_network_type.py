"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

SecondaryNetworkType: TypeAlias = Literal["rdma",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("rdma",))


_VALUES: frozenset[str] = frozenset(("rdma",))


def to_ec2_query_text(value: SecondaryNetworkType) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondaryNetworkType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SecondaryNetworkType value: {text!r}")
    return cast(SecondaryNetworkType, text)


def serialize_ec2_query(
    value: SecondaryNetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondaryNetworkType:
    return from_ec2_query_text(el.text or "")
