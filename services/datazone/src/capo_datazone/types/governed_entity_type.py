"""Generated from Smithy shape ``com.amazonaws.datazone#GovernedEntityType``."""

from typing import Literal, TypeAlias, cast

GovernedEntityType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedEntityType) -> str:
    return value


def deserialize_json(data: str) -> GovernedEntityType:
    return cast(GovernedEntityType, data)
