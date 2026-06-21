"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

ScheduledActionState: TypeAlias = Literal[
    "ACTIVE",
    "DISABLED",
]


# --- awsQuery ser/de ---
def to_query_text(value: ScheduledActionState) -> str:
    return value


def from_query_text(text: str) -> ScheduledActionState:
    return cast(ScheduledActionState, text)


def serialize_query(
    value: ScheduledActionState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduledActionState:
    return from_query_text(el.text or "")
