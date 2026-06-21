"""Generated from Smithy shape ``com.amazonaws.ec2#ApplianceModeSupportValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ApplianceModeSupportValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ApplianceModeSupportValue) -> str:
    return value


def from_ec2_query_text(text: str) -> ApplianceModeSupportValue:
    return cast(ApplianceModeSupportValue, text)


def serialize_ec2_query(
    value: ApplianceModeSupportValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ApplianceModeSupportValue:
    return from_ec2_query_text(el.text or "")
