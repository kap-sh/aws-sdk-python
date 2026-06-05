"""Generated from Smithy shape ``com.amazonaws.ec2#ClientCertificateRevocationListStatusCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ClientCertificateRevocationListStatusCode: TypeAlias = Literal[
    "pending",
    "active",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "active",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "active",
    )
)


def to_ec2_query_text(value: ClientCertificateRevocationListStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientCertificateRevocationListStatusCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ClientCertificateRevocationListStatusCode value: {text!r}"
        )
    return cast(ClientCertificateRevocationListStatusCode, text)


def serialize_ec2_query(
    value: ClientCertificateRevocationListStatusCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientCertificateRevocationListStatusCode:
    return from_ec2_query_text(el.text or "")
