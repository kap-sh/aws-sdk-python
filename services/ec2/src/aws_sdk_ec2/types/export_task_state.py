"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ExportTaskState: TypeAlias = Literal[
    "active",
    "cancelling",
    "cancelled",
    "completed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "cancelling",
        "cancelled",
        "completed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "cancelling",
        "cancelled",
        "completed",
    )
)


def to_ec2_query_text(value: ExportTaskState) -> str:
    return value


def from_ec2_query_text(text: str) -> ExportTaskState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ExportTaskState value: {text!r}")
    return cast(ExportTaskState, text)


def serialize_ec2_query(
    value: ExportTaskState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ExportTaskState:
    return from_ec2_query_text(el.text or "")
