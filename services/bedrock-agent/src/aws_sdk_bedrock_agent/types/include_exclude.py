"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IncludeExclude``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

IncludeExclude: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: IncludeExclude) -> str:
    return value


def deserialize_json(data: str) -> IncludeExclude:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeExclude value: {data!r}")
    return cast(IncludeExclude, data)
