"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ExportTaskState: TypeAlias = Literal[
    "active",
    "cancelling",
    "cancelled",
    "completed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ExportTaskState) -> str:
    return value


def from_ec2_query_text(text: str) -> ExportTaskState:
    return cast(ExportTaskState, text)


def serialize_ec2_query(
    value: ExportTaskState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ExportTaskState:
    return from_ec2_query_text(el.text or "")
