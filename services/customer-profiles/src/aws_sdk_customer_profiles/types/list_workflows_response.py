"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.workflow_list


class ListWorkflowsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_customer_profiles.types.workflow_list.WorkflowList"]
    """<p>List containing workflow details.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.workflow_list

        out["Items"] = aws_sdk_customer_profiles.types.workflow_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.workflow_list

        out["items"] = aws_sdk_customer_profiles.types.workflow_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
