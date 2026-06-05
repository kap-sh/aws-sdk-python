"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceHealthStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceHealthStatus: TypeAlias = Literal[
    "healthy",
    "unhealthy",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "healthy",
        "unhealthy",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "healthy",
        "unhealthy",
    )
)


def to_ec2_query_text(value: InstanceHealthStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceHealthStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InstanceHealthStatus value: {text!r}")
    return cast(InstanceHealthStatus, text)


def serialize_ec2_query(
    value: InstanceHealthStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceHealthStatus:
    return from_ec2_query_text(el.text or "")
