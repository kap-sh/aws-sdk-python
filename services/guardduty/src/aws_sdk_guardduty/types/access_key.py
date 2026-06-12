"""Generated from Smithy shape ``com.amazonaws.guardduty#AccessKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class AccessKey(TypedDict):
    principal_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Principal ID of the user.</p>"""
    user_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Name of the user.</p>"""
    user_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Type of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessKey) -> dict:
    out: dict = {}
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "user_type" in value:
        out["userType"] = value["user_type"]
    return out


def deserialize_json(data: dict) -> AccessKey:
    out: AccessKey = {}  # type: ignore[typeddict-item]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "userType" in data:
        out["user_type"] = data["userType"]
    return out
