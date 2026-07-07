"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_artifacts
    import aws_sdk_cleanrooms.types.analysis_template_text


class _AnalysisSource_text(TypedDict, closed=True):
    text: "aws_sdk_cleanrooms.types.analysis_template_text.AnalysisTemplateText"


class _AnalysisSource_artifacts(TypedDict, closed=True):
    artifacts: (
        "aws_sdk_cleanrooms.types.analysis_template_artifacts.AnalysisTemplateArtifacts"
    )


AnalysisSource: TypeAlias = _AnalysisSource_text | _AnalysisSource_artifacts


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSource) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "artifacts" in value:
        import aws_sdk_cleanrooms.types.analysis_template_artifacts

        return {
            "artifacts": aws_sdk_cleanrooms.types.analysis_template_artifacts.serialize_json(
                value["artifacts"]
            )
        }
    else:
        raise SerializationError("AnalysisSource: no variant present")


def deserialize_json(data: dict) -> AnalysisSource:
    if "text" in data:
        return {"text": data["text"]}
    elif "artifacts" in data:
        import aws_sdk_cleanrooms.types.analysis_template_artifacts

        return {
            "artifacts": aws_sdk_cleanrooms.types.analysis_template_artifacts.deserialize_json(
                data["artifacts"]
            )
        }
    else:
        raise DeserializationError("AnalysisSource: no recognized variant key")
