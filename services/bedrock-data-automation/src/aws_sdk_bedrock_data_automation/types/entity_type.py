"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Entity types supported in DataAutomationLibraries"""
EntityType: TypeAlias = Literal["VOCABULARY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VOCABULARY",))


def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
