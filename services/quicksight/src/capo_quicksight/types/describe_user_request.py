"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.user_name


class DescribeUserRequest(TypedDict, closed=True):
    user_name: "capo_quicksight.types.user_name.UserName"
    """<p>The name of the user that you want to describe.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the user is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace. Currently, you should set this to <code>default</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeUserRequest:
    out: DescribeUserRequest = {}  # type: ignore[typeddict-item]
    return out
