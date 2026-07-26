"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationCategory``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RecommendationCategory) -> str:
    return value


def deserialize_json(data: str) -> RecommendationCategory:
    return cast(RecommendationCategory, data)
