"""Generated from Smithy shape ``com.amazonaws.ec2#BundleTaskState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

BundleTaskState: TypeAlias = Literal[
    "pending",
    "waiting-for-shutdown",
    "bundling",
    "storing",
    "cancelling",
    "complete",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "waiting-for-shutdown",
        "bundling",
        "storing",
        "cancelling",
        "complete",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "waiting-for-shutdown",
        "bundling",
        "storing",
        "cancelling",
        "complete",
        "failed",
    )
)


def to_ec2_query_text(value: BundleTaskState) -> str:
    return value


def from_ec2_query_text(text: str) -> BundleTaskState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BundleTaskState value: {text!r}")
    return cast(BundleTaskState, text)


def serialize_ec2_query(
    value: BundleTaskState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BundleTaskState:
    return from_ec2_query_text(el.text or "")
