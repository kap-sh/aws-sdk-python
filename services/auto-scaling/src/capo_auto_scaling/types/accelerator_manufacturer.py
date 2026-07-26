"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorManufacturer``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

AcceleratorManufacturer: TypeAlias = Literal[
    "nvidia",
    "amd",
    "amazon-web-services",
    "xilinx",
]


# --- awsQuery ser/de ---
def to_query_text(value: AcceleratorManufacturer) -> str:
    return value


def from_query_text(text: str) -> AcceleratorManufacturer:
    return cast(AcceleratorManufacturer, text)


def serialize_query(
    value: AcceleratorManufacturer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AcceleratorManufacturer:
    return from_query_text(el.text or "")
