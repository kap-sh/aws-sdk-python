"""Generated from Smithy shape ``com.amazonaws.ec2#VerificationMethod``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VerificationMethod: TypeAlias = Literal[
    "remarks-x509",
    "dns-token",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "remarks-x509",
        "dns-token",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "remarks-x509",
        "dns-token",
    )
)


def to_ec2_query_text(value: VerificationMethod) -> str:
    return value


def from_ec2_query_text(text: str) -> VerificationMethod:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VerificationMethod value: {text!r}")
    return cast(VerificationMethod, text)


def serialize_ec2_query(
    value: VerificationMethod, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VerificationMethod:
    return from_ec2_query_text(el.text or "")
