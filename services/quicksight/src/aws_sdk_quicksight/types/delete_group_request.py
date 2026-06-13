"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.namespace


class DeleteGroupRequest(TypedDict):
    group_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to delete.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace of the group that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGroupRequest:
    out: DeleteGroupRequest = {}  # type: ignore[typeddict-item]
    return out
