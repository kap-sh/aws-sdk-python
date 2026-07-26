"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#SecurityGroupIdentifier``."""

from typing_extensions import NotRequired, TypedDict


class SecurityGroupIdentifier(TypedDict, closed=True):
    group_id: NotRequired["str"]
    """<p>The security group ID.</p>"""
    group_name: NotRequired["str"]
    """<p>The security group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdentifier) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    return out


def deserialize_json(data: dict) -> SecurityGroupIdentifier:
    out: SecurityGroupIdentifier = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    return out
