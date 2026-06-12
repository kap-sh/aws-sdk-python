"""Generated from Smithy shape ``com.amazonaws.chime#InviteUsersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.user_email_list
    import aws_sdk_chime.types.user_type


class InviteUsersRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_email_list: "aws_sdk_chime.types.user_email_list.UserEmailList"
    """<p>The user email addresses to which to send the email invitation.</p>"""
    user_type: NotRequired["aws_sdk_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteUsersRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.user_email_list

    out["UserEmailList"] = aws_sdk_chime.types.user_email_list.serialize_json(
        value["user_email_list"]
    )
    if "user_type" in value:
        import aws_sdk_chime.types.user_type

        out["UserType"] = aws_sdk_chime.types.user_type.serialize_json(
            value["user_type"]
        )
    return out


def deserialize_json(data: dict) -> InviteUsersRequest:
    out: InviteUsersRequest = {}  # type: ignore[typeddict-item]
    if "UserEmailList" in data:
        import aws_sdk_chime.types.user_email_list

        out["user_email_list"] = aws_sdk_chime.types.user_email_list.deserialize_json(
            data["UserEmailList"]
        )
    else:
        raise DeserializationError("InviteUsersRequest.user_email_list required")
    if "UserType" in data:
        import aws_sdk_chime.types.user_type

        out["user_type"] = aws_sdk_chime.types.user_type.deserialize_json(
            data["UserType"]
        )
    return out
