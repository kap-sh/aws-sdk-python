"""Generated from Smithy shape ``com.amazonaws.ec2#BatchState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

BatchState: TypeAlias = Literal[
    "submitted",
    "active",
    "cancelled",
    "failed",
    "cancelled_running",
    "cancelled_terminating",
    "modifying",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: BatchState) -> str:
    return value


def from_ec2_query_text(text: str) -> BatchState:
    return cast(BatchState, text)


def serialize_ec2_query(
    value: BatchState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BatchState:
    return from_ec2_query_text(el.text or "")
