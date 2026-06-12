"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

IntegrationType: TypeAlias = Literal[
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEND_FINDINGS_TO_SECURITY_HUB",
        "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
        "UPDATE_FINDINGS_IN_SECURITY_HUB",
    )
)


def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationType value: {data!r}")
    return cast(IntegrationType, data)
