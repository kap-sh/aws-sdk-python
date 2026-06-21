"""Generated from Smithy shape ``com.amazonaws.autoscaling#BareMetal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

BareMetal: TypeAlias = Literal[
    "included",
    "excluded",
    "required",
]


# --- awsQuery ser/de ---
def to_query_text(value: BareMetal) -> str:
    return value


def from_query_text(text: str) -> BareMetal:
    return cast(BareMetal, text)


def serialize_query(
    value: BareMetal, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BareMetal:
    return from_query_text(el.text or "")
