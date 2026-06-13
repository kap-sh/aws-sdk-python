"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AnalysisFilterAttribute: TypeAlias = Literal[
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "ANALYSIS_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUICKSIGHT_USER",
        "QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "ANALYSIS_NAME",
    )
)


def serialize_json(value: AnalysisFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> AnalysisFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisFilterAttribute value: {data!r}")
    return cast(AnalysisFilterAttribute, data)
