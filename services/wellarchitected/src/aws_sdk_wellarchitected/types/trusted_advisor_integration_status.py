"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TrustedAdvisorIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

TrustedAdvisorIntegrationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedAdvisorIntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> TrustedAdvisorIntegrationStatus:
    return cast(TrustedAdvisorIntegrationStatus, data)
