"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.access_string
    import aws_sdk_memorydb.types.authentication_mode
    import aws_sdk_memorydb.types.tag_list
    import aws_sdk_memorydb.types.user_name


class CreateUserRequest(TypedDict, closed=True):
    user_name: "aws_sdk_memorydb.types.user_name.UserName"
    """<p>The name of the user. This value must be unique as it also serves as the user identifier.</p>"""
    authentication_mode: "aws_sdk_memorydb.types.authentication_mode.AuthenticationMode"
    """<p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>"""
    access_string: "aws_sdk_memorydb.types.access_string.AccessString"
    """<p>Access permissions string used for this user.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    import aws_sdk_memorydb.types.authentication_mode

    out["AuthenticationMode"] = (
        aws_sdk_memorydb.types.authentication_mode.serialize_aws_json_1_1(
            value["authentication_mode"]
        )
    )
    out["AccessString"] = value["access_string"]
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("CreateUserRequest.user_name required")
    if "AuthenticationMode" in data:
        import aws_sdk_memorydb.types.authentication_mode

        out["authentication_mode"] = (
            aws_sdk_memorydb.types.authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    else:
        raise DeserializationError("CreateUserRequest.authentication_mode required")
    if "AccessString" in data:
        out["access_string"] = data["AccessString"]
    else:
        raise DeserializationError("CreateUserRequest.access_string required")
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
