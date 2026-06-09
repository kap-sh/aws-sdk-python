"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRuleField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TrafficMirrorFilterRuleField: TypeAlias = Literal[
    "destination-port-range",
    "source-port-range",
    "protocol",
    "description",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "destination-port-range",
        "source-port-range",
        "protocol",
        "description",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "destination-port-range",
        "source-port-range",
        "protocol",
        "description",
    )
)


def to_ec2_query_text(value: TrafficMirrorFilterRuleField) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficMirrorFilterRuleField:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TrafficMirrorFilterRuleField value: {text!r}"
        )
    return cast(TrafficMirrorFilterRuleField, text)


def serialize_ec2_query(
    value: TrafficMirrorFilterRuleField, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficMirrorFilterRuleField:
    return from_ec2_query_text(el.text or "")
