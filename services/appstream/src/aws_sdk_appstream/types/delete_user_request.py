"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.authentication_type
    import aws_sdk_appstream.types.username


class DeleteUserRequest(TypedDict):
    user_name: NotRequired["aws_sdk_appstream.types.username.Username"]
    """<p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>"""
    authentication_type: NotRequired[
        "aws_sdk_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user. You must specify USERPOOL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "authentication_type" in value:
        import aws_sdk_appstream.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "AuthenticationType" in data:
        import aws_sdk_appstream.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out
