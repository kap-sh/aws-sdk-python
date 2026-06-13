"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIAMPolicyAssignmentsForUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user_name


class ListIAMPolicyAssignmentsForUserRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the assignments.</p>"""
    user_name: "aws_sdk_quicksight.types.user_name.UserName"
    """<p>The name of the user.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace of the assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIAMPolicyAssignmentsForUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIAMPolicyAssignmentsForUserRequest:
    out: ListIAMPolicyAssignmentsForUserRequest = {}  # type: ignore[typeddict-item]
    return out
