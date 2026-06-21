"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ClientVpnAuthenticationType: TypeAlias = Literal[
    "certificate-authentication",
    "directory-service-authentication",
    "federated-authentication",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ClientVpnAuthenticationType) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnAuthenticationType:
    return cast(ClientVpnAuthenticationType, text)


def serialize_ec2_query(
    value: ClientVpnAuthenticationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnAuthenticationType:
    return from_ec2_query_text(el.text or "")
