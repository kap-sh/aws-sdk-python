"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.user_name


class DeleteUserRequest(TypedDict):
    user_name: "aws_sdk_memorydb.types.user_name.UserName"
    """<p>The name of the user to delete</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("DeleteUserRequest.user_name required")
    return out
