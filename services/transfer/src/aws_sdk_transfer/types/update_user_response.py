"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.user_name


class UpdateUserResponse(TypedDict, closed=True):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a Transfer Family server instance that the account is assigned to.</p>"""
    user_name: "aws_sdk_transfer.types.user_name.UserName"
    """<p>The unique identifier for a user that is assigned to a server instance that was specified in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("UpdateUserResponse.server_id required")
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("UpdateUserResponse.user_name required")
    return out
