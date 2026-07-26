"""Generated from Smithy shape ``com.amazonaws.ec2#Ec2InstanceConnectEndpointState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

Ec2InstanceConnectEndpointState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
    "update-in-progress",
    "update-complete",
    "update-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Ec2InstanceConnectEndpointState) -> str:
    return value


def from_ec2_query_text(text: str) -> Ec2InstanceConnectEndpointState:
    return cast(Ec2InstanceConnectEndpointState, text)


def serialize_ec2_query(
    value: Ec2InstanceConnectEndpointState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Ec2InstanceConnectEndpointState:
    return from_ec2_query_text(el.text or "")
