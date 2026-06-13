"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_detail

AnalysisTemplateValidationStatusDetailList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.analysis_template_validation_status_detail.AnalysisTemplateValidationStatusDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusDetailList) -> list:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_validation_status_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalysisTemplateValidationStatusDetailList:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_detail

    out: AnalysisTemplateValidationStatusDetailList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_validation_status_detail.deserialize_json(
                item
            )
        )
    return out
