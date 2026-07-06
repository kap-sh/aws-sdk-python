"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSourceEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_source_template


class AnalysisSourceEntity(TypedDict, closed=True):
    source_template: NotRequired[
        "aws_sdk_quicksight.types.analysis_source_template.AnalysisSourceTemplate"
    ]
    """<p>The source template for the source entity of the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSourceEntity) -> dict:
    out: dict = {}
    if "source_template" in value:
        import aws_sdk_quicksight.types.analysis_source_template

        out["SourceTemplate"] = (
            aws_sdk_quicksight.types.analysis_source_template.serialize_json(
                value["source_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisSourceEntity:
    out: AnalysisSourceEntity = {}  # type: ignore[typeddict-item]
    if "SourceTemplate" in data:
        import aws_sdk_quicksight.types.analysis_source_template

        out["source_template"] = (
            aws_sdk_quicksight.types.analysis_source_template.deserialize_json(
                data["SourceTemplate"]
            )
        )
    return out
