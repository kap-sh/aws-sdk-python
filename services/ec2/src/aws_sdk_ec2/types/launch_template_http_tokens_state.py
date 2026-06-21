"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateHttpTokensState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

LaunchTemplateHttpTokensState: TypeAlias = Literal[
    "optional",
    "required",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: LaunchTemplateHttpTokensState) -> str:
    return value


def from_ec2_query_text(text: str) -> LaunchTemplateHttpTokensState:
    return cast(LaunchTemplateHttpTokensState, text)


def serialize_ec2_query(
    value: LaunchTemplateHttpTokensState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LaunchTemplateHttpTokensState:
    return from_ec2_query_text(el.text or "")
