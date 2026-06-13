"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.max_results_integer_for_list_applications
    import aws_sdk_qbusiness.types.next_token


class ListApplicationsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business applications.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_applications.MaxResultsIntegerForListApplications"
    ]
    """<p>The maximum number of Amazon Q Business applications to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
