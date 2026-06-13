"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ContentQualityAnalysisState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ContentQualityAnalysisState: TypeAlias = Literal[
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


def serialize_json(value: ContentQualityAnalysisState) -> str:
    return value


def deserialize_json(data: str) -> ContentQualityAnalysisState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContentQualityAnalysisState value: {data!r}"
        )
    return cast(ContentQualityAnalysisState, data)
