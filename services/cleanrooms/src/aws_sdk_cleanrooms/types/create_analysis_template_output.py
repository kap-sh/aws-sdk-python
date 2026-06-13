"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateAnalysisTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template


class CreateAnalysisTemplateOutput(TypedDict):
    analysis_template: "aws_sdk_cleanrooms.types.analysis_template.AnalysisTemplate"
    """<p>The analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalysisTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_template

    out["analysisTemplate"] = aws_sdk_cleanrooms.types.analysis_template.serialize_json(
        value["analysis_template"]
    )
    return out


def deserialize_json(data: dict) -> CreateAnalysisTemplateOutput:
    out: CreateAnalysisTemplateOutput = {}  # type: ignore[typeddict-item]
    if "analysisTemplate" in data:
        import aws_sdk_cleanrooms.types.analysis_template

        out["analysis_template"] = (
            aws_sdk_cleanrooms.types.analysis_template.deserialize_json(
                data["analysisTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAnalysisTemplateOutput.analysis_template required"
        )
    return out
