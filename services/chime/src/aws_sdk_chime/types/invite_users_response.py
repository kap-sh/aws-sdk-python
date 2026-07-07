"""Generated from Smithy shape ``com.amazonaws.chime#InviteUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.invite_list


class InviteUsersResponse(TypedDict, closed=True):
    invites: NotRequired["aws_sdk_chime.types.invite_list.InviteList"]
    """<p>The email invitation details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteUsersResponse) -> dict:
    out: dict = {}
    if "invites" in value:
        import aws_sdk_chime.types.invite_list

        out["Invites"] = aws_sdk_chime.types.invite_list.serialize_json(
            value["invites"]
        )
    return out


def deserialize_json(data: dict) -> InviteUsersResponse:
    out: InviteUsersResponse = {}  # type: ignore[typeddict-item]
    if "Invites" in data:
        import aws_sdk_chime.types.invite_list

        out["invites"] = aws_sdk_chime.types.invite_list.deserialize_json(
            data["Invites"]
        )
    return out
