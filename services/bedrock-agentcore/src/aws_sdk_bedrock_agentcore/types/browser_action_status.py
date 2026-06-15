"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The status of a browser action execution.</p>"""
BrowserActionStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILED",
    )
)


def serialize_json(value: BrowserActionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserActionStatus value: {data!r}")
    return cast(BrowserActionStatus, data)
