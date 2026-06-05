"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ServiceState: TypeAlias = Literal[
    "Pending",
    "Available",
    "Deleting",
    "Deleted",
    "Failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Available",
        "Deleting",
        "Deleted",
        "Failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Available",
        "Deleting",
        "Deleted",
        "Failed",
    )
)


def to_ec2_query_text(value: ServiceState) -> str:
    return value


def from_ec2_query_text(text: str) -> ServiceState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceState value: {text!r}")
    return cast(ServiceState, text)


def serialize_ec2_query(
    value: ServiceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ServiceState:
    return from_ec2_query_text(el.text or "")
