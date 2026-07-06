"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.user_name


class DeleteUserRequest(TypedDict, closed=True):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server instance that has the user assigned to it.</p>"""
    user_name: "aws_sdk_transfer.types.user_name.UserName"
    """<p>A unique string that identifies a user that is being deleted from a server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DeleteUserRequest.server_id required")
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("DeleteUserRequest.user_name required")
    return out
