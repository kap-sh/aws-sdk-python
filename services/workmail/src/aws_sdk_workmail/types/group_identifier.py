"""Generated from Smithy shape ``com.amazonaws.workmail#GroupIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.group_name
    import aws_sdk_workmail.types.work_mail_identifier


class GroupIdentifier(TypedDict):
    group_id: NotRequired[
        "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>Group ID that matched the group.</p>"""
    group_name: NotRequired["aws_sdk_workmail.types.group_name.GroupName"]
    """<p>Group name that matched the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupIdentifier) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupIdentifier:
    out: GroupIdentifier = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    return out
