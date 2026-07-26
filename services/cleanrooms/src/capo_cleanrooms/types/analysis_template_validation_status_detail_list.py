"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_validation_status_detail

AnalysisTemplateValidationStatusDetailList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_template_validation_status_detail.AnalysisTemplateValidationStatusDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusDetailList) -> list:
    import capo_cleanrooms.types.analysis_template_validation_status_detail

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.analysis_template_validation_status_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalysisTemplateValidationStatusDetailList:
    import capo_cleanrooms.types.analysis_template_validation_status_detail

    out: AnalysisTemplateValidationStatusDetailList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.analysis_template_validation_status_detail.deserialize_json(
                item
            )
        )
    return out
