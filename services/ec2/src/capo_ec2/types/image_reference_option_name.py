"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReferenceOptionName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ImageReferenceOptionName: TypeAlias = Literal[
    "state-name",
    "version-depth",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ImageReferenceOptionName) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageReferenceOptionName:
    return cast(ImageReferenceOptionName, text)


def serialize_ec2_query(
    value: ImageReferenceOptionName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageReferenceOptionName:
    return from_ec2_query_text(el.text or "")
