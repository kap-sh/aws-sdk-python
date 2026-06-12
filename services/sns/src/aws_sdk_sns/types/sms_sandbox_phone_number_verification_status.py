"""Generated from Smithy shape ``com.amazonaws.sns#SMSSandboxPhoneNumberVerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

"""Enum listing out all supported destination phone number verification statuses. The following enum values are supported. 1. PENDING : The destination phone number is pending verification. 2. VERIFIED : The destination phone number is verified."""
SMSSandboxPhoneNumberVerificationStatus: TypeAlias = Literal[
    "Pending",
    "Verified",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Verified",
    )
)


def to_query_text(value: SMSSandboxPhoneNumberVerificationStatus) -> str:
    return value


def from_query_text(text: str) -> SMSSandboxPhoneNumberVerificationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown SMSSandboxPhoneNumberVerificationStatus value: {text!r}"
        )
    return cast(SMSSandboxPhoneNumberVerificationStatus, text)


def serialize_query(
    value: SMSSandboxPhoneNumberVerificationStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SMSSandboxPhoneNumberVerificationStatus:
    return from_query_text(el.text or "")
