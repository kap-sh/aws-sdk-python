"""Generated from Smithy shape ``com.amazonaws.rds#TargetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

TargetState: TypeAlias = Literal[
    "REGISTERING",
    "AVAILABLE",
    "UNAVAILABLE",
    "UNUSED",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetState) -> str:
    return value


def from_query_text(text: str) -> TargetState:
    return cast(TargetState, text)


def serialize_query(
    value: TargetState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetState:
    return from_query_text(el.text or "")
