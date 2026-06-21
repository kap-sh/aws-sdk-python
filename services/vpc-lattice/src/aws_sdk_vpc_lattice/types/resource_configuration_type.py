"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceConfigurationType``."""

from typing import Literal, TypeAlias, cast

ResourceConfigurationType: TypeAlias = Literal[
    "GROUP",
    "CHILD",
    "SINGLE",
    "ARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ResourceConfigurationType:
    return cast(ResourceConfigurationType, data)
