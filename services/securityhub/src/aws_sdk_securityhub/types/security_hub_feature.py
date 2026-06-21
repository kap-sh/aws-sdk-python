"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityHubFeature``."""

from typing import Literal, TypeAlias, cast

SecurityHubFeature: TypeAlias = Literal[
    "SecurityHub",
    "SecurityHubV2",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityHubFeature) -> str:
    return value


def deserialize_json(data: str) -> SecurityHubFeature:
    return cast(SecurityHubFeature, data)
