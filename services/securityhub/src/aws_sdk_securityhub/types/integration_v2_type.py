"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegrationV2Type``."""

from typing import Literal, TypeAlias, cast

IntegrationV2Type: TypeAlias = Literal[
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
    "EXTENDED_PLAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationV2Type) -> str:
    return value


def deserialize_json(data: str) -> IntegrationV2Type:
    return cast(IntegrationV2Type, data)
