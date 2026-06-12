"""Generated from Smithy shape ``com.amazonaws.amplify#ListBranchesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.max_results
    import aws_sdk_amplify.types.next_token


class ListBranchesRequest(TypedDict):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p>A pagination token. Set to null to start listing branches from the start. If a non-null pagination token is returned in a result, pass its value in here to list more branches. </p>"""
    max_results: "aws_sdk_amplify.types.max_results.MaxResults"
    """<p> The maximum number of records to list in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBranchesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBranchesRequest:
    out: ListBranchesRequest = {}  # type: ignore[typeddict-item]
    return out
