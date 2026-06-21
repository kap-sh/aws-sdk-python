"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociationResultStatusCode``."""

from typing import Literal, TypeAlias, cast

AssociationResultStatusCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "ACCESS_DENIED",
    "SCAN_CONFIGURATION_NOT_FOUND",
    "INVALID_INPUT",
    "RESOURCE_NOT_FOUND",
    "QUOTA_EXCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationResultStatusCode) -> str:
    return value


def deserialize_json(data: str) -> AssociationResultStatusCode:
    return cast(AssociationResultStatusCode, data)
