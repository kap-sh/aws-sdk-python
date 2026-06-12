"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RequireConfirmation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

"""<p>Whether the action requires user confirmation.</p>"""
RequireConfirmation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: RequireConfirmation) -> str:
    return value


def deserialize_json(data: str) -> RequireConfirmation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequireConfirmation value: {data!r}")
    return cast(RequireConfirmation, data)
