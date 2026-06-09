"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorManufacturer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AcceleratorManufacturer: TypeAlias = Literal[
    "amazon-web-services",
    "amd",
    "nvidia",
    "xilinx",
    "habana",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "amazon-web-services",
        "amd",
        "nvidia",
        "xilinx",
        "habana",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "amazon-web-services",
        "amd",
        "nvidia",
        "xilinx",
        "habana",
    )
)


def to_ec2_query_text(value: AcceleratorManufacturer) -> str:
    return value


def from_ec2_query_text(text: str) -> AcceleratorManufacturer:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorManufacturer value: {text!r}")
    return cast(AcceleratorManufacturer, text)


def serialize_ec2_query(
    value: AcceleratorManufacturer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AcceleratorManufacturer:
    return from_ec2_query_text(el.text or "")
