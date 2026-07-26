"""Generated from Smithy shape ``com.amazonaws.ec2#ResetImageAttributeName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ResetImageAttributeName: TypeAlias = Literal["launchPermission",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ResetImageAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> ResetImageAttributeName:
    return cast(ResetImageAttributeName, text)


def serialize_ec2_query(
    value: ResetImageAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ResetImageAttributeName:
    return from_ec2_query_text(el.text or "")
