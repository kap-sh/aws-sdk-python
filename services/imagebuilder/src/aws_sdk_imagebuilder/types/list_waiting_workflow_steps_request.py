"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWaitingWorkflowStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.restricted_integer


class ListWaitingWorkflowStepsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWaitingWorkflowStepsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWaitingWorkflowStepsRequest:
    out: ListWaitingWorkflowStepsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
