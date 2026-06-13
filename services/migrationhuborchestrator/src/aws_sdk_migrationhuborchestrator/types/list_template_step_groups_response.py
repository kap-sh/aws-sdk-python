"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListTemplateStepGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.template_step_group_summary_list


class ListTemplateStepGroupsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    template_step_group_summary: "aws_sdk_migrationhuborchestrator.types.template_step_group_summary_list.TemplateStepGroupSummaryList"
    """<p>The summary of the step group in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateStepGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_migrationhuborchestrator.types.template_step_group_summary_list

    out["templateStepGroupSummary"] = (
        aws_sdk_migrationhuborchestrator.types.template_step_group_summary_list.serialize_json(
            value["template_step_group_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTemplateStepGroupsResponse:
    out: ListTemplateStepGroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "templateStepGroupSummary" in data:
        import aws_sdk_migrationhuborchestrator.types.template_step_group_summary_list

        out["template_step_group_summary"] = (
            aws_sdk_migrationhuborchestrator.types.template_step_group_summary_list.deserialize_json(
                data["templateStepGroupSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ListTemplateStepGroupsResponse.template_step_group_summary required"
        )
    return out
