"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorManufacturer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

AcceleratorManufacturer: TypeAlias = Literal[
    "nvidia",
    "amd",
    "amazon-web-services",
    "xilinx",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nvidia",
        "amd",
        "amazon-web-services",
        "xilinx",
    )
)


def to_query_text(value: AcceleratorManufacturer) -> str:
    return value


def from_query_text(text: str) -> AcceleratorManufacturer:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorManufacturer value: {text!r}")
    return cast(AcceleratorManufacturer, text)


def serialize_query(
    value: AcceleratorManufacturer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AcceleratorManufacturer:
    return from_query_text(el.text or "")
