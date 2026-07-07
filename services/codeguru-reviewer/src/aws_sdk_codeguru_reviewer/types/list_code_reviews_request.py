"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListCodeReviewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.job_states
    import aws_sdk_codeguru_reviewer.types.list_code_reviews_max_results
    import aws_sdk_codeguru_reviewer.types.next_token
    import aws_sdk_codeguru_reviewer.types.provider_types
    import aws_sdk_codeguru_reviewer.types.repository_names
    import aws_sdk_codeguru_reviewer.types.type


class ListCodeReviewsRequest(TypedDict, closed=True):
    provider_types: NotRequired[
        "aws_sdk_codeguru_reviewer.types.provider_types.ProviderTypes"
    ]
    """<p>List of provider types for filtering that needs to be applied before displaying the result. For example, <code>providerTypes=[GitHub]</code> lists code reviews from GitHub.</p>"""
    states: NotRequired["aws_sdk_codeguru_reviewer.types.job_states.JobStates"]
    """<p>List of states for filtering that needs to be applied before displaying the result. For example, <code>states=[Pending]</code> lists code reviews in the Pending state.</p> <p>The valid code review states are:</p> <ul> <li> <p> <code>Completed</code>: The code review is complete.</p> </li> <li> <p> <code>Pending</code>: The code review started and has not completed or failed.</p> </li> <li> <p> <code>Failed</code>: The code review failed.</p> </li> <li> <p> <code>Deleting</code>: The code review is being deleted.</p> </li> </ul>"""
    repository_names: NotRequired[
        "aws_sdk_codeguru_reviewer.types.repository_names.RepositoryNames"
    ]
    """<p>List of repository names for filtering that needs to be applied before displaying the result.</p>"""
    type: "aws_sdk_codeguru_reviewer.types.type.Type"
    """<p>The type of code reviews to list in the response.</p>"""
    max_results: NotRequired[
        "aws_sdk_codeguru_reviewer.types.list_code_reviews_max_results.ListCodeReviewsMaxResults"
    ]
    """<p>The maximum number of results that are returned per call. The default is 100.</p>"""
    next_token: NotRequired["aws_sdk_codeguru_reviewer.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeReviewsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodeReviewsRequest:
    out: ListCodeReviewsRequest = {}  # type: ignore[typeddict-item]
    return out
