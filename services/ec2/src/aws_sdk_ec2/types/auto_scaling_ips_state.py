"""Generated from Smithy shape ``com.amazonaws.ec2#AutoScalingIpsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AutoScalingIpsState: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def to_ec2_query_text(value: AutoScalingIpsState) -> str:
    return value


def from_ec2_query_text(text: str) -> AutoScalingIpsState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AutoScalingIpsState value: {text!r}")
    return cast(AutoScalingIpsState, text)


def serialize_ec2_query(
    value: AutoScalingIpsState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AutoScalingIpsState:
    return from_ec2_query_text(el.text or "")
