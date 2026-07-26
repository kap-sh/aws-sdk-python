"""Generated from Smithy shape ``com.amazonaws.ec2#ConversionTaskState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ConversionTaskState: TypeAlias = Literal[
    "active",
    "cancelling",
    "cancelled",
    "completed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ConversionTaskState) -> str:
    return value


def from_ec2_query_text(text: str) -> ConversionTaskState:
    return cast(ConversionTaskState, text)


def serialize_ec2_query(
    value: ConversionTaskState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ConversionTaskState:
    return from_ec2_query_text(el.text or "")
