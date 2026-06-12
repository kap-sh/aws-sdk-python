"""Generated from Smithy shape ``com.amazonaws.novaact#ListSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.max_results
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.sort_order
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name


class ListSessionsRequest(TypedDict):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the workflow run.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run to list sessions for.</p>"""
    max_results: NotRequired["aws_sdk_nova_act.types.max_results.MaxResults"]
    """<p>The maximum number of sessions to return in a single response.</p>"""
    next_token: NotRequired["aws_sdk_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results.</p>"""
    sort_order: NotRequired["aws_sdk_nova_act.types.sort_order.SortOrder"]
    """<p>The sort order for the returned sessions (ascending or descending).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsRequest) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import aws_sdk_nova_act.types.sort_order

        out["sortOrder"] = aws_sdk_nova_act.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> ListSessionsRequest:
    out: ListSessionsRequest = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_nova_act.types.sort_order

        out["sort_order"] = aws_sdk_nova_act.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    return out
