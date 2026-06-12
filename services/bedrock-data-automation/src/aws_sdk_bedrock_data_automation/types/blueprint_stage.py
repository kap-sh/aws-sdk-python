"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Stage of the Blueprint"""
BlueprintStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPMENT",
        "LIVE",
    )
)


def serialize_json(value: BlueprintStage) -> str:
    return value


def deserialize_json(data: str) -> BlueprintStage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintStage value: {data!r}")
    return cast(BlueprintStage, data)
