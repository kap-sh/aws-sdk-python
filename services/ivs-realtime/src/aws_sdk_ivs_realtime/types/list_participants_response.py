"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.participant_list


class ListParticipantsResponse(TypedDict):
    participants: "aws_sdk_ivs_realtime.types.participant_list.ParticipantList"
    """<p>List of the matching participants (summary information only).</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more participants than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.participant_list

    out["participants"] = aws_sdk_ivs_realtime.types.participant_list.serialize_json(
        value["participants"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListParticipantsResponse:
    out: ListParticipantsResponse = {}  # type: ignore[typeddict-item]
    if "participants" in data:
        import aws_sdk_ivs_realtime.types.participant_list

        out["participants"] = (
            aws_sdk_ivs_realtime.types.participant_list.deserialize_json(
                data["participants"]
            )
        )
    else:
        raise DeserializationError("ListParticipantsResponse.participants required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
