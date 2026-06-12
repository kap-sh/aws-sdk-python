"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

HandshakeResourceType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
    "ORGANIZATION_FEATURE_SET",
    "EMAIL",
    "MASTER_EMAIL",
    "MASTER_NAME",
    "NOTES",
    "PARENT_HANDSHAKE",
    "RESPONSIBILITY_TRANSFER",
    "TRANSFER_START_TIMESTAMP",
    "TRANSFER_TYPE",
    "MANAGEMENT_ACCOUNT",
    "MANAGEMENT_EMAIL",
    "MANAGEMENT_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORGANIZATION",
        "ORGANIZATION_FEATURE_SET",
        "EMAIL",
        "MASTER_EMAIL",
        "MASTER_NAME",
        "NOTES",
        "PARENT_HANDSHAKE",
        "RESPONSIBILITY_TRANSFER",
        "TRANSFER_START_TIMESTAMP",
        "TRANSFER_TYPE",
        "MANAGEMENT_ACCOUNT",
        "MANAGEMENT_EMAIL",
        "MANAGEMENT_NAME",
    )
)


def serialize_aws_json_1_1(value: HandshakeResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HandshakeResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HandshakeResourceType value: {data!r}")
    return cast(HandshakeResourceType, data)
