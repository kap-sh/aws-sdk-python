"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_error

AnalysisErrorList: TypeAlias = list[
    "capo_quicksight.types.analysis_error.AnalysisError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisErrorList) -> list:
    import capo_quicksight.types.analysis_error

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.analysis_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisErrorList:
    import capo_quicksight.types.analysis_error

    out: AnalysisErrorList = []
    for item in data:
        out.append(capo_quicksight.types.analysis_error.deserialize_json(item))
    return out
