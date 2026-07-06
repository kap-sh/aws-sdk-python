"""Generated from Smithy shape ``com.amazonaws.chime#ListRoomMembershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.room_membership_list
    import aws_sdk_chime.types.string


class ListRoomMembershipsResponse(TypedDict, closed=True):
    room_memberships: NotRequired[
        "aws_sdk_chime.types.room_membership_list.RoomMembershipList"
    ]
    """<p>The room membership details.</p>"""
    next_token: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomMembershipsResponse) -> dict:
    out: dict = {}
    if "room_memberships" in value:
        import aws_sdk_chime.types.room_membership_list

        out["RoomMemberships"] = (
            aws_sdk_chime.types.room_membership_list.serialize_json(
                value["room_memberships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoomMembershipsResponse:
    out: ListRoomMembershipsResponse = {}  # type: ignore[typeddict-item]
    if "RoomMemberships" in data:
        import aws_sdk_chime.types.room_membership_list

        out["room_memberships"] = (
            aws_sdk_chime.types.room_membership_list.deserialize_json(
                data["RoomMemberships"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
