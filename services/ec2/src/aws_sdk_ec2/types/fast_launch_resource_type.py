"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

FastLaunchResourceType: TypeAlias = Literal["snapshot",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FastLaunchResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> FastLaunchResourceType:
    return cast(FastLaunchResourceType, text)


def serialize_ec2_query(
    value: FastLaunchResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FastLaunchResourceType:
    return from_ec2_query_text(el.text or "")
