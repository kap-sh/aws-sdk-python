"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityType``."""

from typing import Literal, TypeAlias, cast

"""Entity types supported in DataAutomationLibraries"""
EntityType: TypeAlias = Literal["VOCABULARY",]


# --- restJson1 ser/de ---
def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    return cast(EntityType, data)
