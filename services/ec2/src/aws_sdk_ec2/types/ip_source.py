"""Generated from Smithy shape ``com.amazonaws.ec2#IpSource``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IpSource: TypeAlias = Literal[
    "amazon",
    "byoip",
    "none",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "amazon",
        "byoip",
        "none",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "amazon",
        "byoip",
        "none",
    )
)


def to_ec2_query_text(value: IpSource) -> str:
    return value


def from_ec2_query_text(text: str) -> IpSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpSource value: {text!r}")
    return cast(IpSource, text)


def serialize_ec2_query(
    value: IpSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpSource:
    return from_ec2_query_text(el.text or "")
