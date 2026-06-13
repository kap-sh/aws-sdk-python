"""Generated from Smithy shape ``com.amazonaws.datazone#IamUserProfileDetails``."""

from typing import TypedDict
from typing_extensions import NotRequired


class IamUserProfileDetails(TypedDict):
    arn: NotRequired["str"]
    """<p>The ARN of the IAM user.</p>"""
    principal_id: NotRequired["str"]
    """<p>The principal ID as part of the IAM user profile details.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""
    group_profile_id: NotRequired["str"]
    """<p>The identifier of the group profile associated with the IAM user profile. This links the user to a specific group profile within the Amazon DataZone domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamUserProfileDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "group_profile_id" in value:
        out["groupProfileId"] = value["group_profile_id"]
    return out


def deserialize_json(data: dict) -> IamUserProfileDetails:
    out: IamUserProfileDetails = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    if "sessionName" in data:
        out["session_name"] = data["sessionName"]
    if "groupProfileId" in data:
        out["group_profile_id"] = data["groupProfileId"]
    return out
