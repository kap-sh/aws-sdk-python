"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

AcceleratorName: TypeAlias = Literal[
    "a100",
    "v100",
    "k80",
    "t4",
    "m60",
    "radeon-pro-v520",
    "vu9p",
]


# --- awsQuery ser/de ---
def to_query_text(value: AcceleratorName) -> str:
    return value


def from_query_text(text: str) -> AcceleratorName:
    return cast(AcceleratorName, text)


def serialize_query(
    value: AcceleratorName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AcceleratorName:
    return from_query_text(el.text or "")
