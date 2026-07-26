"""Generated from Smithy shape ``com.amazonaws.ec2#ImageState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ImageState: TypeAlias = Literal[
    "pending",
    "available",
    "invalid",
    "deregistered",
    "transient",
    "failed",
    "error",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ImageState) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageState:
    return cast(ImageState, text)


def serialize_ec2_query(
    value: ImageState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageState:
    return from_ec2_query_text(el.text or "")
