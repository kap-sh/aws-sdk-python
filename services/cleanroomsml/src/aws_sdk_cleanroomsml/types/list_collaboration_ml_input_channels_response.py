"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationMLInputChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_ml_input_channels_list
    import aws_sdk_cleanroomsml.types.next_token


class ListCollaborationMLInputChannelsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_ml_input_channels_list: "aws_sdk_cleanroomsml.types.collaboration_ml_input_channels_list.CollaborationMLInputChannelsList"
    """<p>The list of ML input channels that you wanted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationMLInputChannelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.collaboration_ml_input_channels_list

    out["collaborationMLInputChannelsList"] = (
        aws_sdk_cleanroomsml.types.collaboration_ml_input_channels_list.serialize_json(
            value["collaboration_ml_input_channels_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationMLInputChannelsResponse:
    out: ListCollaborationMLInputChannelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationMLInputChannelsList" in data:
        import aws_sdk_cleanroomsml.types.collaboration_ml_input_channels_list

        out["collaboration_ml_input_channels_list"] = (
            aws_sdk_cleanroomsml.types.collaboration_ml_input_channels_list.deserialize_json(
                data["collaborationMLInputChannelsList"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationMLInputChannelsResponse.collaboration_ml_input_channels_list required"
        )
    return out
