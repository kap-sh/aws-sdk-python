"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyPolicyTier``."""

from typing import Literal, TypeAlias, cast

ResiliencyPolicyTier: TypeAlias = Literal[
    "MissionCritical",
    "Critical",
    "Important",
    "CoreServices",
    "NonCritical",
    "NotApplicable",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResiliencyPolicyTier) -> str:
    return value


def deserialize_json(data: str) -> ResiliencyPolicyTier:
    return cast(ResiliencyPolicyTier, data)
