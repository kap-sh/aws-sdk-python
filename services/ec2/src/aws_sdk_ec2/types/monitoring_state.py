"""Generated from Smithy shape ``com.amazonaws.ec2#MonitoringState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

MonitoringState: TypeAlias = Literal[
    "disabled",
    "disabling",
    "enabled",
    "pending",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "disabling",
        "enabled",
        "pending",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "disabling",
        "enabled",
        "pending",
    )
)


def to_ec2_query_text(value: MonitoringState) -> str:
    return value


def from_ec2_query_text(text: str) -> MonitoringState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MonitoringState value: {text!r}")
    return cast(MonitoringState, text)


def serialize_ec2_query(
    value: MonitoringState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MonitoringState:
    return from_ec2_query_text(el.text or "")
