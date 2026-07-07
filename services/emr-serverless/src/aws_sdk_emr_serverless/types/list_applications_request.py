"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_state_set
    import aws_sdk_emr_serverless.types.next_token


class ListApplicationsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The token for the next set of application results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of applications that can be listed.</p>"""
    states: NotRequired[
        "aws_sdk_emr_serverless.types.application_state_set.ApplicationStateSet"
    ]
    """<p>An optional filter for application states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
