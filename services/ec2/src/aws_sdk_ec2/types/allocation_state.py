"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

AllocationState: TypeAlias = Literal[
    "available",
    "under-assessment",
    "permanent-failure",
    "released",
    "released-permanent-failure",
    "pending",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "under-assessment",
        "permanent-failure",
        "released",
        "released-permanent-failure",
        "pending",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "under-assessment",
        "permanent-failure",
        "released",
        "released-permanent-failure",
        "pending",
    )
)


def to_ec2_query_text(value: AllocationState) -> str:
    return value


def from_ec2_query_text(text: str) -> AllocationState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AllocationState value: {text!r}")
    return cast(AllocationState, text)


def serialize_ec2_query(
    value: AllocationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AllocationState:
    return from_ec2_query_text(el.text or "")
