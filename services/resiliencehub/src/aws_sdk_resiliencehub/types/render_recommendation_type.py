"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RenderRecommendationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

RenderRecommendationType: TypeAlias = Literal[
    "Alarm",
    "Sop",
    "Test",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Alarm",
        "Sop",
        "Test",
    )
)


def serialize_json(value: RenderRecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RenderRecommendationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RenderRecommendationType value: {data!r}")
    return cast(RenderRecommendationType, data)
