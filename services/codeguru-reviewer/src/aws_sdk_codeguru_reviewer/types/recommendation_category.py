"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

RecommendationCategory: TypeAlias = Literal[
    "AWSBestPractices",
    "AWSCloudFormationIssues",
    "DuplicateCode",
    "CodeMaintenanceIssues",
    "ConcurrencyIssues",
    "InputValidations",
    "PythonBestPractices",
    "JavaBestPractices",
    "ResourceLeaks",
    "SecurityIssues",
    "CodeInconsistencies",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWSBestPractices",
        "AWSCloudFormationIssues",
        "DuplicateCode",
        "CodeMaintenanceIssues",
        "ConcurrencyIssues",
        "InputValidations",
        "PythonBestPractices",
        "JavaBestPractices",
        "ResourceLeaks",
        "SecurityIssues",
        "CodeInconsistencies",
    )
)


def serialize_json(value: RecommendationCategory) -> str:
    return value


def deserialize_json(data: str) -> RecommendationCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationCategory value: {data!r}")
    return cast(RecommendationCategory, data)
