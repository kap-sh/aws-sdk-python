"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FeatureType``."""

from typing import Literal, TypeAlias, cast

FeatureType: TypeAlias = Literal[
    "TEXTUAL",
    "CATEGORICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureType) -> str:
    return value


def deserialize_json(data: str) -> FeatureType:
    return cast(FeatureType, data)
