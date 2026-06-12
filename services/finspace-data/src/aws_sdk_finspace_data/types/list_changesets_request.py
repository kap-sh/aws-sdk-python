"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListChangesetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.dataset_id
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.result_limit


class ListChangesetsRequest(TypedDict):
    dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the FinSpace Dataset to which the Changeset belongs.</p>"""
    max_results: NotRequired["aws_sdk_finspace_data.types.result_limit.ResultLimit"]
    """<p>The maximum number of results per page.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangesetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChangesetsRequest:
    out: ListChangesetsRequest = {}  # type: ignore[typeddict-item]
    return out
