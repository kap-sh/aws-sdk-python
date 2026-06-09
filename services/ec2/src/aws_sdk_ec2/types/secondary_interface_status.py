"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

SecondaryInterfaceStatus: TypeAlias = Literal[
    "available",
    "in-use",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "in-use",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "in-use",
    )
)


def to_ec2_query_text(value: SecondaryInterfaceStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondaryInterfaceStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SecondaryInterfaceStatus value: {text!r}")
    return cast(SecondaryInterfaceStatus, text)


def serialize_ec2_query(
    value: SecondaryInterfaceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondaryInterfaceStatus:
    return from_ec2_query_text(el.text or "")
