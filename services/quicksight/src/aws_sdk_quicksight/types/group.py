"""Generated from Smithy shape ``com.amazonaws.quicksight#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.group_description
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.string


class Group(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the group.</p>"""
    group_name: NotRequired["aws_sdk_quicksight.types.group_name.GroupName"]
    """<p>The name of the group.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.group_description.GroupDescription"
    ]
    """<p>The group description.</p>"""
    principal_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The principal ID of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    return out
