"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

SubnetState: TypeAlias = Literal[
    "pending",
    "available",
    "unavailable",
    "failed",
    "failed-insufficient-capacity",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "unavailable",
        "failed",
        "failed-insufficient-capacity",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "unavailable",
        "failed",
        "failed-insufficient-capacity",
    )
)


def to_ec2_query_text(value: SubnetState) -> str:
    return value


def from_ec2_query_text(text: str) -> SubnetState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SubnetState value: {text!r}")
    return cast(SubnetState, text)


def serialize_ec2_query(
    value: SubnetState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SubnetState:
    return from_ec2_query_text(el.text or "")
