"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListTemplateStepGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.template_id


class ListTemplateStepGroupsRequest(TypedDict):
    max_results: "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateStepGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplateStepGroupsRequest:
    out: ListTemplateStepGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
