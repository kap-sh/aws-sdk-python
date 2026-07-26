"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ConnectionNotificationType: TypeAlias = Literal["Topic",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ConnectionNotificationType) -> str:
    return value


def from_ec2_query_text(text: str) -> ConnectionNotificationType:
    return cast(ConnectionNotificationType, text)


def serialize_ec2_query(
    value: ConnectionNotificationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ConnectionNotificationType:
    return from_ec2_query_text(el.text or "")
