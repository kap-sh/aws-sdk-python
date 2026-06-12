"""Generated from Smithy shape ``com.amazonaws.securityhub#ListInvitationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.cross_account_max_results
    import aws_sdk_securityhub.types.next_token


class ListInvitationsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
    ]
    """<p>The maximum number of items to return in the response. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>ListInvitations</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInvitationsRequest:
    out: ListInvitationsRequest = {}  # type: ignore[typeddict-item]
    return out
