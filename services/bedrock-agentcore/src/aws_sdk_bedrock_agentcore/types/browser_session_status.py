"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

BrowserSessionStatus: TypeAlias = Literal[
    "READY",
    "TERMINATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "TERMINATED",
    )
)


def serialize_json(value: BrowserSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserSessionStatus value: {data!r}")
    return cast(BrowserSessionStatus, data)
