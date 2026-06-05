"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerMonitoredTagKeyStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

CapacityManagerMonitoredTagKeyStatus: TypeAlias = Literal[
    "activating",
    "activated",
    "deactivating",
    "suspended",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "activating",
        "activated",
        "deactivating",
        "suspended",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "activating",
        "activated",
        "deactivating",
        "suspended",
    )
)


def to_ec2_query_text(value: CapacityManagerMonitoredTagKeyStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityManagerMonitoredTagKeyStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityManagerMonitoredTagKeyStatus value: {text!r}"
        )
    return cast(CapacityManagerMonitoredTagKeyStatus, text)


def serialize_ec2_query(
    value: CapacityManagerMonitoredTagKeyStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityManagerMonitoredTagKeyStatus:
    return from_ec2_query_text(el.text or "")
