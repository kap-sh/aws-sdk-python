"""Generated from Smithy shape ``com.amazonaws.repostspace#FeatureEnableStatus``."""

from typing import Literal, TypeAlias, cast

FeatureEnableStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "NOT_ALLOWED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureEnableStatus) -> str:
    return value


def deserialize_json(data: str) -> FeatureEnableStatus:
    return cast(FeatureEnableStatus, data)
