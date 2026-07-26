"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegrationType``."""

from typing import Literal, TypeAlias, cast

IntegrationType: TypeAlias = Literal[
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    return cast(IntegrationType, data)
