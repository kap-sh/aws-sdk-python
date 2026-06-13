"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateSourceEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.template_source_analysis
    import aws_sdk_quicksight.types.template_source_template


class TemplateSourceEntity(TypedDict):
    source_analysis: NotRequired[
        "aws_sdk_quicksight.types.template_source_analysis.TemplateSourceAnalysis"
    ]
    """<p>The source analysis, if it is based on an analysis.</p>"""
    source_template: NotRequired[
        "aws_sdk_quicksight.types.template_source_template.TemplateSourceTemplate"
    ]
    """<p>The source template, if it is based on an template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSourceEntity) -> dict:
    out: dict = {}
    if "source_analysis" in value:
        import aws_sdk_quicksight.types.template_source_analysis

        out["SourceAnalysis"] = (
            aws_sdk_quicksight.types.template_source_analysis.serialize_json(
                value["source_analysis"]
            )
        )
    if "source_template" in value:
        import aws_sdk_quicksight.types.template_source_template

        out["SourceTemplate"] = (
            aws_sdk_quicksight.types.template_source_template.serialize_json(
                value["source_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemplateSourceEntity:
    out: TemplateSourceEntity = {}  # type: ignore[typeddict-item]
    if "SourceAnalysis" in data:
        import aws_sdk_quicksight.types.template_source_analysis

        out["source_analysis"] = (
            aws_sdk_quicksight.types.template_source_analysis.deserialize_json(
                data["SourceAnalysis"]
            )
        )
    if "SourceTemplate" in data:
        import aws_sdk_quicksight.types.template_source_template

        out["source_template"] = (
            aws_sdk_quicksight.types.template_source_template.deserialize_json(
                data["SourceTemplate"]
            )
        )
    return out
