"""Generated from Smithy shape ``com.amazonaws.securityhub#ListMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.cross_account_max_results
    import aws_sdk_securityhub.types.next_token


class ListMembersRequest(TypedDict, closed=True):
    only_associated: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies which member accounts to include in the response based on their relationship status with the administrator account. The default value is <code>TRUE</code>.</p> <p>If <code>OnlyAssociated</code> is set to <code>TRUE</code>, the response includes member accounts whose relationship status with the administrator account is set to <code>ENABLED</code>.</p> <p>If <code>OnlyAssociated</code> is set to <code>FALSE</code>, the response includes all existing member accounts. </p>"""
    max_results: NotRequired[
        "aws_sdk_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
    ]
    """<p>The maximum number of items to return in the response. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>ListMembers</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMembersRequest:
    out: ListMembersRequest = {}  # type: ignore[typeddict-item]
    return out
