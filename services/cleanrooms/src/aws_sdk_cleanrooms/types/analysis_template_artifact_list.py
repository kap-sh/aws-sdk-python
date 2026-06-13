"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_artifact

AnalysisTemplateArtifactList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.analysis_template_artifact.AnalysisTemplateArtifact"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateArtifactList) -> list:
    import aws_sdk_cleanrooms.types.analysis_template_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_artifact.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalysisTemplateArtifactList:
    import aws_sdk_cleanrooms.types.analysis_template_artifact

    out: AnalysisTemplateArtifactList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_artifact.deserialize_json(item)
        )
    return out
