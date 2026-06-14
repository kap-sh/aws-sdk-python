"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The type of recommendation to generate.</p>"""
RecommendationType: TypeAlias = Literal[
    "SYSTEM_PROMPT_RECOMMENDATION",
    "TOOL_DESCRIPTION_RECOMMENDATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM_PROMPT_RECOMMENDATION",
        "TOOL_DESCRIPTION_RECOMMENDATION",
    )
)


def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationType value: {data!r}")
    return cast(RecommendationType, data)
