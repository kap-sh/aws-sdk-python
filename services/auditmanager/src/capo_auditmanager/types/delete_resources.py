"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteResources``."""

from typing import Literal, TypeAlias, cast

DeleteResources: TypeAlias = Literal[
    "ALL",
    "DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResources) -> str:
    return value


def deserialize_json(data: str) -> DeleteResources:
    return cast(DeleteResources, data)
