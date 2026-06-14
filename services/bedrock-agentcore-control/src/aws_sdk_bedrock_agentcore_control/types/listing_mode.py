"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ListingMode: TypeAlias = Literal[
    "DEFAULT",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "DYNAMIC",
    )
)


def serialize_json(value: ListingMode) -> str:
    return value


def deserialize_json(data: str) -> ListingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListingMode value: {data!r}")
    return cast(ListingMode, data)
