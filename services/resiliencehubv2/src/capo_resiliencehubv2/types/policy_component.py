"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyComponent``."""

from typing import Literal, TypeAlias, cast

PolicyComponent: TypeAlias = Literal[
    "AVAILABILITY_SLO",
    "MULTI_AZ_DISASTER_RECOVERY",
    "MULTI_REGION_DISASTER_RECOVERY",
    "DATA_RECOVERY",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyComponent) -> str:
    return value


def deserialize_json(data: str) -> PolicyComponent:
    return cast(PolicyComponent, data)
