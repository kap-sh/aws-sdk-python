"""Generated from Smithy shape ``com.amazonaws.ec2#ClientCertificateRevocationListStatusCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ClientCertificateRevocationListStatusCode: TypeAlias = Literal[
    "pending",
    "active",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ClientCertificateRevocationListStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientCertificateRevocationListStatusCode:
    return cast(ClientCertificateRevocationListStatusCode, text)


def serialize_ec2_query(
    value: ClientCertificateRevocationListStatusCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientCertificateRevocationListStatusCode:
    return from_ec2_query_text(el.text or "")
