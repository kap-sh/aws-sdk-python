"""Generated from Smithy shape ``com.amazonaws.ec2#DnsNameState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

DnsNameState: TypeAlias = Literal[
    "pendingVerification",
    "verified",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: DnsNameState) -> str:
    return value


def from_ec2_query_text(text: str) -> DnsNameState:
    return cast(DnsNameState, text)


def serialize_ec2_query(
    value: DnsNameState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DnsNameState:
    return from_ec2_query_text(el.text or "")
