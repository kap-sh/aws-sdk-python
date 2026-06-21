"""Generated from Smithy shape ``com.amazonaws.ec2#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

Status: TypeAlias = Literal[
    "MoveInProgress",
    "InVpc",
    "InClassic",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Status) -> str:
    return value


def from_ec2_query_text(text: str) -> Status:
    return cast(Status, text)


def serialize_ec2_query(
    value: Status, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Status:
    return from_ec2_query_text(el.text or "")
