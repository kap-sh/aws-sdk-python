"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SecondaryNetworkState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SecondaryNetworkState) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondaryNetworkState:
    return cast(SecondaryNetworkState, text)


def serialize_ec2_query(
    value: SecondaryNetworkState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondaryNetworkState:
    return from_ec2_query_text(el.text or "")
