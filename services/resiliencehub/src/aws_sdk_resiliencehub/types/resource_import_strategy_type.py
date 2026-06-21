"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceImportStrategyType``."""

from typing import Literal, TypeAlias, cast

ResourceImportStrategyType: TypeAlias = Literal[
    "AddOnly",
    "ReplaceAll",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceImportStrategyType) -> str:
    return value


def deserialize_json(data: str) -> ResourceImportStrategyType:
    return cast(ResourceImportStrategyType, data)
