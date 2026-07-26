"""Generated from Smithy shape ``com.amazonaws.chime#InviteUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.user_email_list
    import capo_chime.types.user_type


class InviteUsersRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_email_list: "capo_chime.types.user_email_list.UserEmailList"
    """<p>The user email addresses to which to send the email invitation.</p>"""
    user_type: NotRequired["capo_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteUsersRequest) -> dict:
    out: dict = {}
    import capo_chime.types.user_email_list

    out["UserEmailList"] = capo_chime.types.user_email_list.serialize_json(
        value["user_email_list"]
    )
    if "user_type" in value:
        import capo_chime.types.user_type

        out["UserType"] = capo_chime.types.user_type.serialize_json(value["user_type"])
    return out


def deserialize_json(data: dict) -> InviteUsersRequest:
    out: InviteUsersRequest = {}  # type: ignore[typeddict-item]
    if "UserEmailList" in data:
        import capo_chime.types.user_email_list

        out["user_email_list"] = capo_chime.types.user_email_list.deserialize_json(
            data["UserEmailList"]
        )
    else:
        raise DeserializationError("InviteUsersRequest.user_email_list required")
    if "UserType" in data:
        import capo_chime.types.user_type

        out["user_type"] = capo_chime.types.user_type.deserialize_json(data["UserType"])
    return out
