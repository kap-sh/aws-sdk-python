"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorRuleAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TrafficMirrorRuleAction: TypeAlias = Literal[
    "accept",
    "reject",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "accept",
        "reject",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "accept",
        "reject",
    )
)


def to_ec2_query_text(value: TrafficMirrorRuleAction) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficMirrorRuleAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TrafficMirrorRuleAction value: {text!r}")
    return cast(TrafficMirrorRuleAction, text)


def serialize_ec2_query(
    value: TrafficMirrorRuleAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficMirrorRuleAction:
    return from_ec2_query_text(el.text or "")
