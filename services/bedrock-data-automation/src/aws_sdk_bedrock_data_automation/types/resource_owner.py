"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Resource Owner"""
ResourceOwner: TypeAlias = Literal[
    "SERVICE",
    "ACCOUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE",
        "ACCOUNT",
    )
)


def serialize_json(value: ResourceOwner) -> str:
    return value


def deserialize_json(data: str) -> ResourceOwner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceOwner value: {data!r}")
    return cast(ResourceOwner, data)
