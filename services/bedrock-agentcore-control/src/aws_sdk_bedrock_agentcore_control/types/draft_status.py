"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DraftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

"""<p> Publish synchronization state of the DRAFT working copy. </p>"""
DraftStatus: TypeAlias = Literal[
    "MODIFIED",
    "UNMODIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODIFIED",
        "UNMODIFIED",
    )
)


def serialize_json(value: DraftStatus) -> str:
    return value


def deserialize_json(data: str) -> DraftStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DraftStatus value: {data!r}")
    return cast(DraftStatus, data)
