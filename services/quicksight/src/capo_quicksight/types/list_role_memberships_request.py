"""Generated from Smithy shape ``com.amazonaws.quicksight#ListRoleMembershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.namespace
    import capo_quicksight.types.role
    import capo_quicksight.types.string


class ListRoleMembershipsRequest(TypedDict, closed=True):
    role: "capo_quicksight.types.role.Role"
    """<p>The name of the role.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create a group in. The Amazon Web Services account ID that you provide must be the same Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that includes the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoleMembershipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRoleMembershipsRequest:
    out: ListRoleMembershipsRequest = {}  # type: ignore[typeddict-item]
    return out
