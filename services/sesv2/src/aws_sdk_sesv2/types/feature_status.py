"""Generated from Smithy shape ``com.amazonaws.sesv2#FeatureStatus``."""

from typing import Literal, TypeAlias, cast

FeatureStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> FeatureStatus:
    return cast(FeatureStatus, data)
