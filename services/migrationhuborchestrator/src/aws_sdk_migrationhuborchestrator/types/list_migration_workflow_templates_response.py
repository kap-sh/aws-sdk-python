"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListMigrationWorkflowTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.template_summary_list


class ListMigrationWorkflowTemplatesResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    template_summary: "aws_sdk_migrationhuborchestrator.types.template_summary_list.TemplateSummaryList"
    """<p>The summary of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationWorkflowTemplatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_migrationhuborchestrator.types.template_summary_list

    out["templateSummary"] = (
        aws_sdk_migrationhuborchestrator.types.template_summary_list.serialize_json(
            value["template_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMigrationWorkflowTemplatesResponse:
    out: ListMigrationWorkflowTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "templateSummary" in data:
        import aws_sdk_migrationhuborchestrator.types.template_summary_list

        out["template_summary"] = (
            aws_sdk_migrationhuborchestrator.types.template_summary_list.deserialize_json(
                data["templateSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ListMigrationWorkflowTemplatesResponse.template_summary required"
        )
    return out
