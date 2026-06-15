"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseButton``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The mouse button to use for a browser mouse action.</p>"""
MouseButton: TypeAlias = Literal[
    "LEFT",
    "RIGHT",
    "MIDDLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEFT",
        "RIGHT",
        "MIDDLE",
    )
)


def serialize_json(value: MouseButton) -> str:
    return value


def deserialize_json(data: str) -> MouseButton:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MouseButton value: {data!r}")
    return cast(MouseButton, data)
