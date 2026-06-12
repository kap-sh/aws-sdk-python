"""Generated from Smithy shape ``com.amazonaws.transfer#UserDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.session_id
    import aws_sdk_transfer.types.user_name


class UserDetails(TypedDict):
    user_name: "aws_sdk_transfer.types.user_name.UserName"
    """<p>A unique string that identifies a Transfer Family user associated with a server.</p>"""
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The system-assigned unique identifier for a Transfer server instance. </p>"""
    session_id: NotRequired["aws_sdk_transfer.types.session_id.SessionId"]
    """<p>The system-assigned unique identifier for a session that corresponds to the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDetails) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    out["ServerId"] = value["server_id"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDetails:
    out: UserDetails = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("UserDetails.user_name required")
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("UserDetails.server_id required")
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    return out
