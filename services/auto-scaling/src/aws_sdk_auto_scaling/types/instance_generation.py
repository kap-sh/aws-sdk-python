"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceGeneration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

InstanceGeneration: TypeAlias = Literal[
    "current",
    "previous",
]


# --- awsQuery ser/de ---
def to_query_text(value: InstanceGeneration) -> str:
    return value


def from_query_text(text: str) -> InstanceGeneration:
    return cast(InstanceGeneration, text)


def serialize_query(
    value: InstanceGeneration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InstanceGeneration:
    return from_query_text(el.text or "")
