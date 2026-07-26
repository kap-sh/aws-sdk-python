"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteUserByPrincipalIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.string


class DeleteUserByPrincipalIdRequest(TypedDict, closed=True):
    principal_id: "capo_quicksight.types.string.String"
    """<p>The principal ID of the user.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the user is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace. Currently, you should set this to <code>default</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserByPrincipalIdRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserByPrincipalIdRequest:
    out: DeleteUserByPrincipalIdRequest = {}  # type: ignore[typeddict-item]
    return out
