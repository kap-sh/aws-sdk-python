"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateSourceEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.template_source_analysis
    import capo_quicksight.types.template_source_template


class TemplateSourceEntity(TypedDict, closed=True):
    source_analysis: NotRequired[
        "capo_quicksight.types.template_source_analysis.TemplateSourceAnalysis"
    ]
    """<p>The source analysis, if it is based on an analysis.</p>"""
    source_template: NotRequired[
        "capo_quicksight.types.template_source_template.TemplateSourceTemplate"
    ]
    """<p>The source template, if it is based on an template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSourceEntity) -> dict:
    out: dict = {}
    if "source_analysis" in value:
        import capo_quicksight.types.template_source_analysis

        out["SourceAnalysis"] = (
            capo_quicksight.types.template_source_analysis.serialize_json(
                value["source_analysis"]
            )
        )
    if "source_template" in value:
        import capo_quicksight.types.template_source_template

        out["SourceTemplate"] = (
            capo_quicksight.types.template_source_template.serialize_json(
                value["source_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemplateSourceEntity:
    out: TemplateSourceEntity = {}  # type: ignore[typeddict-item]
    if "SourceAnalysis" in data:
        import capo_quicksight.types.template_source_analysis

        out["source_analysis"] = (
            capo_quicksight.types.template_source_analysis.deserialize_json(
                data["SourceAnalysis"]
            )
        )
    if "SourceTemplate" in data:
        import capo_quicksight.types.template_source_template

        out["source_template"] = (
            capo_quicksight.types.template_source_template.deserialize_json(
                data["SourceTemplate"]
            )
        )
    return out
