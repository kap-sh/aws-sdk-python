"""Generated from Smithy shape ``com.amazonaws.ec2#TransferType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransferType: TypeAlias = Literal[
    "time-based",
    "standard",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransferType) -> str:
    return value


def from_ec2_query_text(text: str) -> TransferType:
    return cast(TransferType, text)


def serialize_ec2_query(
    value: TransferType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransferType:
    return from_ec2_query_text(el.text or "")
