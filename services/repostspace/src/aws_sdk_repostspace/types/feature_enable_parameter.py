"""Generated from Smithy shape ``com.amazonaws.repostspace#FeatureEnableParameter``."""

from typing import Literal, TypeAlias, cast

FeatureEnableParameter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureEnableParameter) -> str:
    return value


def deserialize_json(data: str) -> FeatureEnableParameter:
    return cast(FeatureEnableParameter, data)
