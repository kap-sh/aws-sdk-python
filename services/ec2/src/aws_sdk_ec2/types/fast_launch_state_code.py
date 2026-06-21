"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

FastLaunchStateCode: TypeAlias = Literal[
    "enabling",
    "enabling-failed",
    "enabled",
    "enabled-failed",
    "disabling",
    "disabling-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FastLaunchStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> FastLaunchStateCode:
    return cast(FastLaunchStateCode, text)


def serialize_ec2_query(
    value: FastLaunchStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FastLaunchStateCode:
    return from_ec2_query_text(el.text or "")
