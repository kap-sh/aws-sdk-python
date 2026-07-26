"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationStatus``."""

from typing import Literal, TypeAlias, cast

AssociationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> AssociationStatus:
    return cast(AssociationStatus, data)
