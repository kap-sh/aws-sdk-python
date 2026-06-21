"""Generated from Smithy shape ``com.amazonaws.ec2#ReportState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ReportState: TypeAlias = Literal[
    "running",
    "cancelled",
    "complete",
    "error",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ReportState) -> str:
    return value


def from_ec2_query_text(text: str) -> ReportState:
    return cast(ReportState, text)


def serialize_ec2_query(
    value: ReportState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReportState:
    return from_ec2_query_text(el.text or "")
