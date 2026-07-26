"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointStatusCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

VerifiedAccessEndpointStatusCode: TypeAlias = Literal[
    "pending",
    "active",
    "updating",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VerifiedAccessEndpointStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> VerifiedAccessEndpointStatusCode:
    return cast(VerifiedAccessEndpointStatusCode, text)


def serialize_ec2_query(
    value: VerifiedAccessEndpointStatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointStatusCode:
    return from_ec2_query_text(el.text or "")
