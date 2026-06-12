"""Generated from Smithy shape ``com.amazonaws.inspector#SecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector.types.text


class SecurityGroup(TypedDict):
    group_name: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The name of the security group.</p>"""
    group_id: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The ID of the security group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroup) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroup:
    out: SecurityGroup = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
