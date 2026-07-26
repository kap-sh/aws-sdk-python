"""Generated from Smithy shape ``com.amazonaws.directoryservice#ResetUserPasswordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.customer_user_name
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.user_password


class ResetUserPasswordRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the Managed Microsoft AD or Simple AD directory in which the user resides.</p>"""
    user_name: "capo_directory_service.types.customer_user_name.CustomerUserName"
    """<p>The user name of the user whose password will be reset.</p>"""
    new_password: "capo_directory_service.types.user_password.UserPassword"
    """<p>The new password that will be reset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetUserPasswordRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["UserName"] = value["user_name"]
    out["NewPassword"] = value["new_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetUserPasswordRequest:
    out: ResetUserPasswordRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("ResetUserPasswordRequest.directory_id required")
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("ResetUserPasswordRequest.user_name required")
    if "NewPassword" in data:
        out["new_password"] = data["NewPassword"]
    else:
        raise DeserializationError("ResetUserPasswordRequest.new_password required")
    return out
