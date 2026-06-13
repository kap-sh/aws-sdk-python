"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIAMPolicyAssignmentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.assignment_status
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string


class ListIAMPolicyAssignmentsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains these IAM policy assignments.</p>"""
    assignment_status: NotRequired[
        "aws_sdk_quicksight.types.assignment_status.AssignmentStatus"
    ]
    """<p>The status of the assignments.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace for the assignments.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIAMPolicyAssignmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIAMPolicyAssignmentsRequest:
    out: ListIAMPolicyAssignmentsRequest = {}  # type: ignore[typeddict-item]
    return out
