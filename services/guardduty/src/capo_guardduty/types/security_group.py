"""Generated from Smithy shape ``com.amazonaws.guardduty#SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class SecurityGroup(TypedDict, closed=True):
    group_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The security group ID of the EC2 instance.</p>"""
    group_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The security group name of the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroup) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    return out


def deserialize_json(data: dict) -> SecurityGroup:
    out: SecurityGroup = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    return out
