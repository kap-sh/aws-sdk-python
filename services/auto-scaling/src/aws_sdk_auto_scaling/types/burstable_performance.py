"""Generated from Smithy shape ``com.amazonaws.autoscaling#BurstablePerformance``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

BurstablePerformance: TypeAlias = Literal[
    "included",
    "excluded",
    "required",
]


# --- awsQuery ser/de ---
def to_query_text(value: BurstablePerformance) -> str:
    return value


def from_query_text(text: str) -> BurstablePerformance:
    return cast(BurstablePerformance, text)


def serialize_query(
    value: BurstablePerformance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BurstablePerformance:
    return from_query_text(el.text or "")
