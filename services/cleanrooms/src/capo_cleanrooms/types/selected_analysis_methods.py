"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SelectedAnalysisMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.selected_analysis_method

SelectedAnalysisMethods: TypeAlias = list[
    "capo_cleanrooms.types.selected_analysis_method.SelectedAnalysisMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedAnalysisMethods) -> list:
    import capo_cleanrooms.types.selected_analysis_method

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.selected_analysis_method.serialize_json(item))
    return out


def deserialize_json(data: list) -> SelectedAnalysisMethods:
    import capo_cleanrooms.types.selected_analysis_method

    out: SelectedAnalysisMethods = []
    for item in data:
        out.append(
            capo_cleanrooms.types.selected_analysis_method.deserialize_json(item)
        )
    return out
