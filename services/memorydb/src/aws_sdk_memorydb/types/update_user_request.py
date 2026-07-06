"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.access_string
    import aws_sdk_memorydb.types.authentication_mode
    import aws_sdk_memorydb.types.user_name


class UpdateUserRequest(TypedDict, closed=True):
    user_name: "aws_sdk_memorydb.types.user_name.UserName"
    """<p>The name of the user</p>"""
    authentication_mode: NotRequired[
        "aws_sdk_memorydb.types.authentication_mode.AuthenticationMode"
    ]
    """<p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>"""
    access_string: NotRequired["aws_sdk_memorydb.types.access_string.AccessString"]
    """<p>Access permissions string used for this user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    if "authentication_mode" in value:
        import aws_sdk_memorydb.types.authentication_mode

        out["AuthenticationMode"] = (
            aws_sdk_memorydb.types.authentication_mode.serialize_aws_json_1_1(
                value["authentication_mode"]
            )
        )
    if "access_string" in value:
        out["AccessString"] = value["access_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("UpdateUserRequest.user_name required")
    if "AuthenticationMode" in data:
        import aws_sdk_memorydb.types.authentication_mode

        out["authentication_mode"] = (
            aws_sdk_memorydb.types.authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    if "AccessString" in data:
        out["access_string"] = data["AccessString"]
    return out
