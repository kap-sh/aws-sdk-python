"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ContributionAnalysisDirection: TypeAlias = Literal[
    "INCREASE",
    "DECREASE",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCREASE",
        "DECREASE",
        "NEUTRAL",
    )
)


def serialize_json(value: ContributionAnalysisDirection) -> str:
    return value


def deserialize_json(data: str) -> ContributionAnalysisDirection:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContributionAnalysisDirection value: {data!r}"
        )
    return cast(ContributionAnalysisDirection, data)
