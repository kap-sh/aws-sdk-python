"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RecommendedStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.recommended_step

RecommendedStepList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.recommended_step.RecommendedStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedStepList) -> list:
    import aws_sdk_accessanalyzer.types.recommended_step

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.recommended_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendedStepList:
    import aws_sdk_accessanalyzer.types.recommended_step

    out: RecommendedStepList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.recommended_step.deserialize_json(item))
    return out
