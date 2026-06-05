"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VpcBlockPublicAccessState: TypeAlias = Literal[
    "default-state",
    "update-in-progress",
    "update-complete",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default-state",
        "update-in-progress",
        "update-complete",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "default-state",
        "update-in-progress",
        "update-complete",
    )
)


def to_ec2_query_text(value: VpcBlockPublicAccessState) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcBlockPublicAccessState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcBlockPublicAccessState value: {text!r}")
    return cast(VpcBlockPublicAccessState, text)


def serialize_ec2_query(
    value: VpcBlockPublicAccessState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcBlockPublicAccessState:
    return from_ec2_query_text(el.text or "")
