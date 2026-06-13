"""Generated from Smithy shape ``com.amazonaws.datazone#GetIamPortalLoginUrlOutput``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError


class GetIamPortalLoginUrlOutput(TypedDict):
    auth_code_url: NotRequired["str"]
    """<p>The data portal URL of the specified Amazon DataZone domain.</p>"""
    user_profile_id: "str"
    """<p>The ID of the user profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIamPortalLoginUrlOutput) -> dict:
    out: dict = {}
    if "auth_code_url" in value:
        out["authCodeUrl"] = value["auth_code_url"]
    out["userProfileId"] = value["user_profile_id"]
    return out


def deserialize_json(data: dict) -> GetIamPortalLoginUrlOutput:
    out: GetIamPortalLoginUrlOutput = {}  # type: ignore[typeddict-item]
    if "authCodeUrl" in data:
        out["auth_code_url"] = data["authCodeUrl"]
    if "userProfileId" in data:
        out["user_profile_id"] = data["userProfileId"]
    else:
        raise DeserializationError(
            "GetIamPortalLoginUrlOutput.user_profile_id required"
        )
    return out
