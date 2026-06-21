"""Generated from Smithy shape ``com.amazonaws.appsync#AssociationStatus``."""

from typing import Literal, TypeAlias, cast

AssociationStatus: TypeAlias = Literal[
    "PROCESSING",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> AssociationStatus:
    return cast(AssociationStatus, data)
