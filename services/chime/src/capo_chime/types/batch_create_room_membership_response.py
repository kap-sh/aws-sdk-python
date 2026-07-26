"""Generated from Smithy shape ``com.amazonaws.chime#BatchCreateRoomMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.member_error_list


class BatchCreateRoomMembershipResponse(TypedDict, closed=True):
    errors: NotRequired["capo_chime.types.member_error_list.MemberErrorList"]
    """<p>If the action fails for one or more of the member IDs in the request, a list of the member IDs is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRoomMembershipResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_chime.types.member_error_list

        out["Errors"] = capo_chime.types.member_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchCreateRoomMembershipResponse:
    out: BatchCreateRoomMembershipResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import capo_chime.types.member_error_list

        out["errors"] = capo_chime.types.member_error_list.deserialize_json(
            data["Errors"]
        )
    return out
