"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantReplicasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.participant_replica_list


class ListParticipantReplicasResponse(TypedDict):
    replicas: (
        "aws_sdk_ivs_realtime.types.participant_replica_list.ParticipantReplicaList"
    )
    """<p>List of all participant replicas.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more participants than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantReplicasResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.participant_replica_list

    out["replicas"] = (
        aws_sdk_ivs_realtime.types.participant_replica_list.serialize_json(
            value["replicas"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListParticipantReplicasResponse:
    out: ListParticipantReplicasResponse = {}  # type: ignore[typeddict-item]
    if "replicas" in data:
        import aws_sdk_ivs_realtime.types.participant_replica_list

        out["replicas"] = (
            aws_sdk_ivs_realtime.types.participant_replica_list.deserialize_json(
                data["replicas"]
            )
        )
    else:
        raise DeserializationError("ListParticipantReplicasResponse.replicas required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
