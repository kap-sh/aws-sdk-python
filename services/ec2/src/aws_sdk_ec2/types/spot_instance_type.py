"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

SpotInstanceType: TypeAlias = Literal[
    "one-time",
    "persistent",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "one-time",
        "persistent",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "one-time",
        "persistent",
    )
)


def to_ec2_query_text(value: SpotInstanceType) -> str:
    return value


def from_ec2_query_text(text: str) -> SpotInstanceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SpotInstanceType value: {text!r}")
    return cast(SpotInstanceType, text)


def serialize_ec2_query(
    value: SpotInstanceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SpotInstanceType:
    return from_ec2_query_text(el.text or "")
