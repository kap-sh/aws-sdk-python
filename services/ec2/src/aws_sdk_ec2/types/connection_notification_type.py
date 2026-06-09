"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ConnectionNotificationType: TypeAlias = Literal["Topic",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("Topic",))


_VALUES: frozenset[str] = frozenset(("Topic",))


def to_ec2_query_text(value: ConnectionNotificationType) -> str:
    return value


def from_ec2_query_text(text: str) -> ConnectionNotificationType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ConnectionNotificationType value: {text!r}"
        )
    return cast(ConnectionNotificationType, text)


def serialize_ec2_query(
    value: ConnectionNotificationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ConnectionNotificationType:
    return from_ec2_query_text(el.text or "")
