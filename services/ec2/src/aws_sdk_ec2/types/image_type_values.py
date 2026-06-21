"""Generated from Smithy shape ``com.amazonaws.ec2#ImageTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ImageTypeValues: TypeAlias = Literal[
    "machine",
    "kernel",
    "ramdisk",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ImageTypeValues) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageTypeValues:
    return cast(ImageTypeValues, text)


def serialize_ec2_query(
    value: ImageTypeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageTypeValues:
    return from_ec2_query_text(el.text or "")
