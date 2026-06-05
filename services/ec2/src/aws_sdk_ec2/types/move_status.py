"""Generated from Smithy shape ``com.amazonaws.ec2#MoveStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

MoveStatus: TypeAlias = Literal[
    "movingToVpc",
    "restoringToClassic",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "movingToVpc",
        "restoringToClassic",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "movingToVpc",
        "restoringToClassic",
    )
)


def to_ec2_query_text(value: MoveStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> MoveStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MoveStatus value: {text!r}")
    return cast(MoveStatus, text)


def serialize_ec2_query(
    value: MoveStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MoveStatus:
    return from_ec2_query_text(el.text or "")
