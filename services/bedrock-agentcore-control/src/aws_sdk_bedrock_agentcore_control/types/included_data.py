"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IncludedData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

IncludedData: TypeAlias = Literal[
    "ALL_DATA",
    "METADATA_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_DATA",
        "METADATA_ONLY",
    )
)


def serialize_json(value: IncludedData) -> str:
    return value


def deserialize_json(data: str) -> IncludedData:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludedData value: {data!r}")
    return cast(IncludedData, data)
