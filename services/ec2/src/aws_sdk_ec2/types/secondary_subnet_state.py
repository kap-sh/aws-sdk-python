"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SecondarySubnetState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SecondarySubnetState) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondarySubnetState:
    return cast(SecondarySubnetState, text)


def serialize_ec2_query(
    value: SecondarySubnetState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondarySubnetState:
    return from_ec2_query_text(el.text or "")
