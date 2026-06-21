"""Generated from Smithy shape ``com.amazonaws.ec2#ImageBlockPublicAccessDisabledState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ImageBlockPublicAccessDisabledState: TypeAlias = Literal["unblocked",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ImageBlockPublicAccessDisabledState) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageBlockPublicAccessDisabledState:
    return cast(ImageBlockPublicAccessDisabledState, text)


def serialize_ec2_query(
    value: ImageBlockPublicAccessDisabledState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageBlockPublicAccessDisabledState:
    return from_ec2_query_text(el.text or "")
