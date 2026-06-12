"""Generated from Smithy shape ``com.amazonaws.chime#DisassociateSigninDelegateGroupsFromAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.non_empty_string_list


class DisassociateSigninDelegateGroupsFromAccountRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    group_names: "aws_sdk_chime.types.non_empty_string_list.NonEmptyStringList"
    """<p>The sign-in delegate group names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateSigninDelegateGroupsFromAccountRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.non_empty_string_list

    out["GroupNames"] = aws_sdk_chime.types.non_empty_string_list.serialize_json(
        value["group_names"]
    )
    return out


def deserialize_json(data: dict) -> DisassociateSigninDelegateGroupsFromAccountRequest:
    out: DisassociateSigninDelegateGroupsFromAccountRequest = {}  # type: ignore[typeddict-item]
    if "GroupNames" in data:
        import aws_sdk_chime.types.non_empty_string_list

        out["group_names"] = aws_sdk_chime.types.non_empty_string_list.deserialize_json(
            data["GroupNames"]
        )
    else:
        raise DeserializationError(
            "DisassociateSigninDelegateGroupsFromAccountRequest.group_names required"
        )
    return out
