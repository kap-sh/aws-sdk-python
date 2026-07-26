"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListTemplateStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.template_step_summary_list


class ListTemplateStepsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    template_step_summary_list: NotRequired[
        "capo_migrationhuborchestrator.types.template_step_summary_list.TemplateStepSummaryList"
    ]
    """<p>The list of summaries of steps in a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateStepsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "template_step_summary_list" in value:
        import capo_migrationhuborchestrator.types.template_step_summary_list

        out["templateStepSummaryList"] = (
            capo_migrationhuborchestrator.types.template_step_summary_list.serialize_json(
                value["template_step_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTemplateStepsResponse:
    out: ListTemplateStepsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "templateStepSummaryList" in data:
        import capo_migrationhuborchestrator.types.template_step_summary_list

        out["template_step_summary_list"] = (
            capo_migrationhuborchestrator.types.template_step_summary_list.deserialize_json(
                data["templateStepSummaryList"]
            )
        )
    return out
