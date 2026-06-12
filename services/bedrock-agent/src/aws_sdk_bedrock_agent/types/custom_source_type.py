"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

CustomSourceType: TypeAlias = Literal[
    "IN_LINE",
    "S3_LOCATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_LINE",
        "S3_LOCATION",
    )
)


def serialize_json(value: CustomSourceType) -> str:
    return value


def deserialize_json(data: str) -> CustomSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomSourceType value: {data!r}")
    return cast(CustomSourceType, data)
