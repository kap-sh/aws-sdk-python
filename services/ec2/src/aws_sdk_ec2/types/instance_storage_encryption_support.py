"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStorageEncryptionSupport``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceStorageEncryptionSupport: TypeAlias = Literal[
    "unsupported",
    "required",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "required",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "required",
    )
)


def to_ec2_query_text(value: InstanceStorageEncryptionSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceStorageEncryptionSupport:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceStorageEncryptionSupport value: {text!r}"
        )
    return cast(InstanceStorageEncryptionSupport, text)


def serialize_ec2_query(
    value: InstanceStorageEncryptionSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceStorageEncryptionSupport:
    return from_ec2_query_text(el.text or "")
