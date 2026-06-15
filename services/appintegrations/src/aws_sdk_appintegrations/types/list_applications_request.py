"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_type
    import aws_sdk_appintegrations.types.max_results
    import aws_sdk_appintegrations.types.next_token


class ListApplicationsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_appintegrations.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    application_type: NotRequired[
        "aws_sdk_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
