"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedImagesSettingsDisabledState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AllowedImagesSettingsDisabledState: TypeAlias = Literal["disabled",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AllowedImagesSettingsDisabledState) -> str:
    return value


def from_ec2_query_text(text: str) -> AllowedImagesSettingsDisabledState:
    return cast(AllowedImagesSettingsDisabledState, text)


def serialize_ec2_query(
    value: AllowedImagesSettingsDisabledState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AllowedImagesSettingsDisabledState:
    return from_ec2_query_text(el.text or "")
