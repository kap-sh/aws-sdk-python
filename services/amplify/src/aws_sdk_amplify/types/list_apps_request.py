"""Generated from Smithy shape ``com.amazonaws.amplify#ListAppsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplify.types.max_results_for_list_apps
    import aws_sdk_amplify.types.next_token


class ListAppsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If non-null, the pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>"""
    max_results: "aws_sdk_amplify.types.max_results_for_list_apps.MaxResultsForListApps"
    """<p>The maximum number of records to list in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppsRequest:
    out: ListAppsRequest = {}  # type: ignore[typeddict-item]
    return out
