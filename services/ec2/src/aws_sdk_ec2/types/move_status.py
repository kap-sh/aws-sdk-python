"""Generated from Smithy shape ``com.amazonaws.ec2#MoveStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

MoveStatus: TypeAlias = Literal[
    "movingToVpc",
    "restoringToClassic",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MoveStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> MoveStatus:
    return cast(MoveStatus, text)


def serialize_ec2_query(
    value: MoveStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MoveStatus:
    return from_ec2_query_text(el.text or "")
