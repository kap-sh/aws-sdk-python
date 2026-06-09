"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ConnectionNotificationState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_ec2_query_text(value: ConnectionNotificationState) -> str:
    return value


def from_ec2_query_text(text: str) -> ConnectionNotificationState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ConnectionNotificationState value: {text!r}"
        )
    return cast(ConnectionNotificationState, text)


def serialize_ec2_query(
    value: ConnectionNotificationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ConnectionNotificationState:
    return from_ec2_query_text(el.text or "")
