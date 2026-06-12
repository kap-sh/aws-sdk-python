"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintStageFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Blueprint Stage filter"""
BlueprintStageFilter: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPMENT",
        "LIVE",
        "ALL",
    )
)


def serialize_json(value: BlueprintStageFilter) -> str:
    return value


def deserialize_json(data: str) -> BlueprintStageFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintStageFilter value: {data!r}")
    return cast(BlueprintStageFilter, data)
