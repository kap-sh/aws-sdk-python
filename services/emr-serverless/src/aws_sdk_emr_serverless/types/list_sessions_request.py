"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.next_token
    import aws_sdk_emr_serverless.types.session_state_set


class ListSessionsRequest(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application to list sessions for.</p>"""
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The token for the next set of session results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of sessions to return in each page of results.</p>"""
    states: NotRequired[
        "aws_sdk_emr_serverless.types.session_state_set.SessionStateSet"
    ]
    """<p>An optional filter for session states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>"""
    created_at_after: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The lower bound of the option to filter by creation date and time.</p>"""
    created_at_before: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The upper bound of the option to filter by creation date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSessionsRequest:
    out: ListSessionsRequest = {}  # type: ignore[typeddict-item]
    return out
