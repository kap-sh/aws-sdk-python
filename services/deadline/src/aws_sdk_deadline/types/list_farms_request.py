"""Generated from Smithy shape ``com.amazonaws.deadline#ListFarmsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.identity_center_principal_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token


class ListFarmsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    principal_id: NotRequired[
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    ]
    """<p>The principal ID of the member to list on the farm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFarmsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFarmsRequest:
    out: ListFarmsRequest = {}  # type: ignore[typeddict-item]
    return out
