"""Generated from Smithy shape ``com.amazonaws.autoscaling#CpuManufacturer``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

CpuManufacturer: TypeAlias = Literal[
    "intel",
    "amd",
    "amazon-web-services",
    "apple",
]


# --- awsQuery ser/de ---
def to_query_text(value: CpuManufacturer) -> str:
    return value


def from_query_text(text: str) -> CpuManufacturer:
    return cast(CpuManufacturer, text)


def serialize_query(
    value: CpuManufacturer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CpuManufacturer:
    return from_query_text(el.text or "")
