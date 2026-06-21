"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

AcceleratorType: TypeAlias = Literal[
    "gpu",
    "fpga",
    "inference",
]


# --- awsQuery ser/de ---
def to_query_text(value: AcceleratorType) -> str:
    return value


def from_query_text(text: str) -> AcceleratorType:
    return cast(AcceleratorType, text)


def serialize_query(
    value: AcceleratorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AcceleratorType:
    return from_query_text(el.text or "")
