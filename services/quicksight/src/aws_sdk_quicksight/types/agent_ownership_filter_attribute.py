"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentOwnershipFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AgentOwnershipFilterAttribute: TypeAlias = Literal[
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "AGENT_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "AGENT_NAME",
    )
)


def serialize_json(value: AgentOwnershipFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> AgentOwnershipFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AgentOwnershipFilterAttribute value: {data!r}"
        )
    return cast(AgentOwnershipFilterAttribute, data)
