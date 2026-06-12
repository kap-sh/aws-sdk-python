"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationTemplateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

RecommendationTemplateStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Failed",
        "Success",
    )
)


def serialize_json(value: RecommendationTemplateStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationTemplateStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RecommendationTemplateStatus value: {data!r}"
        )
    return cast(RecommendationTemplateStatus, data)
