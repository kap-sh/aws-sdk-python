"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IntegratingService``."""

from typing import Literal, TypeAlias, cast

IntegratingService: TypeAlias = Literal["JIRA",]


# --- restJson1 ser/de ---
def serialize_json(value: IntegratingService) -> str:
    return value


def deserialize_json(data: str) -> IntegratingService:
    return cast(IntegratingService, data)
