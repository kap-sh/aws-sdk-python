"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisSortType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ContributionAnalysisSortType: TypeAlias = Literal[
    "ABSOLUTE_DIFFERENCE",
    "CONTRIBUTION_PERCENTAGE",
    "DEVIATION_FROM_EXPECTED",
    "PERCENTAGE_DIFFERENCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ABSOLUTE_DIFFERENCE",
        "CONTRIBUTION_PERCENTAGE",
        "DEVIATION_FROM_EXPECTED",
        "PERCENTAGE_DIFFERENCE",
    )
)


def serialize_json(value: ContributionAnalysisSortType) -> str:
    return value


def deserialize_json(data: str) -> ContributionAnalysisSortType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContributionAnalysisSortType value: {data!r}"
        )
    return cast(ContributionAnalysisSortType, data)
