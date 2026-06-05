"""Generated from Smithy shape ``com.amazonaws.ec2#EncryptionSupportOptionValue``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

EncryptionSupportOptionValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


def to_ec2_query_text(value: EncryptionSupportOptionValue) -> str:
    return value


def from_ec2_query_text(text: str) -> EncryptionSupportOptionValue:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown EncryptionSupportOptionValue value: {text!r}"
        )
    return cast(EncryptionSupportOptionValue, text)


def serialize_ec2_query(
    value: EncryptionSupportOptionValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EncryptionSupportOptionValue:
    return from_ec2_query_text(el.text or "")
