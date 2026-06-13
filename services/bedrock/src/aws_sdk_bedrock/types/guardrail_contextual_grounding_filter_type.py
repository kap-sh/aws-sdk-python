"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailContextualGroundingFilterType: TypeAlias = Literal[
    "GROUNDING",
    "RELEVANCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROUNDING",
        "RELEVANCE",
    )
)


def serialize_json(value: GuardrailContextualGroundingFilterType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContextualGroundingFilterType value: {data!r}"
        )
    return cast(GuardrailContextualGroundingFilterType, data)
