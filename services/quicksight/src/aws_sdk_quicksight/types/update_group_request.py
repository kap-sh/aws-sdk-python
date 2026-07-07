"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_description
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.namespace


class UpdateGroupRequest(TypedDict, closed=True):
    group_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.group_description.GroupDescription"
    ]
    """<p>The description for the group that you want to update.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace of the group that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
