"""Generated from Smithy shape ``com.amazonaws.novaact#ListWorkflowDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.max_results
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.sort_order


class ListWorkflowDefinitionsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_nova_act.types.max_results.MaxResults"]
    """<p>The maximum number of workflow definitions to return in a single response.</p>"""
    next_token: NotRequired["aws_sdk_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results.</p>"""
    sort_order: NotRequired["aws_sdk_nova_act.types.sort_order.SortOrder"]
    """<p>The sort order for the returned workflow definitions (ascending or descending).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowDefinitionsRequest) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import aws_sdk_nova_act.types.sort_order

        out["sortOrder"] = aws_sdk_nova_act.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> ListWorkflowDefinitionsRequest:
    out: ListWorkflowDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_nova_act.types.sort_order

        out["sort_order"] = aws_sdk_nova_act.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    return out
