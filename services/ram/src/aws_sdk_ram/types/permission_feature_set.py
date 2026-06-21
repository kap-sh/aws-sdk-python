"""Generated from Smithy shape ``com.amazonaws.ram#PermissionFeatureSet``."""

from typing import Literal, TypeAlias, cast

PermissionFeatureSet: TypeAlias = Literal[
    "CREATED_FROM_POLICY",
    "PROMOTING_TO_STANDARD",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionFeatureSet) -> str:
    return value


def deserialize_json(data: str) -> PermissionFeatureSet:
    return cast(PermissionFeatureSet, data)
