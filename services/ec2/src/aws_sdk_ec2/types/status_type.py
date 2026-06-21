"""Generated from Smithy shape ``com.amazonaws.ec2#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

StatusType: TypeAlias = Literal[
    "passed",
    "failed",
    "insufficient-data",
    "initializing",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: StatusType) -> str:
    return value


def from_ec2_query_text(text: str) -> StatusType:
    return cast(StatusType, text)


def serialize_ec2_query(
    value: StatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StatusType:
    return from_ec2_query_text(el.text or "")
