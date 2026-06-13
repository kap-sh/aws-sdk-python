"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_error

AnalysisErrorList: TypeAlias = list[
    "aws_sdk_quicksight.types.analysis_error.AnalysisError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisErrorList) -> list:
    import aws_sdk_quicksight.types.analysis_error

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.analysis_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisErrorList:
    import aws_sdk_quicksight.types.analysis_error

    out: AnalysisErrorList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.analysis_error.deserialize_json(item))
    return out
