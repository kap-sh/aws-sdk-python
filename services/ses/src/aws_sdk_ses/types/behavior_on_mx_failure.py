"""Generated from Smithy shape ``com.amazonaws.ses#BehaviorOnMXFailure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element

BehaviorOnMXFailure: TypeAlias = Literal[
    "UseDefaultValue",
    "RejectMessage",
]


# --- awsQuery ser/de ---
def to_query_text(value: BehaviorOnMXFailure) -> str:
    return value


def from_query_text(text: str) -> BehaviorOnMXFailure:
    return cast(BehaviorOnMXFailure, text)


def serialize_query(
    value: BehaviorOnMXFailure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BehaviorOnMXFailure:
    return from_query_text(el.text or "")
