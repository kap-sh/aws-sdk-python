"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

"""<p>The status of a browser profile.</p>"""
BrowserProfileStatus: TypeAlias = Literal[
    "READY",
    "DELETING",
    "DELETED",
    "SAVING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "DELETING",
        "DELETED",
        "SAVING",
    )
)


def serialize_json(value: BrowserProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserProfileStatus value: {data!r}")
    return cast(BrowserProfileStatus, data)
