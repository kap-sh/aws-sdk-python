"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationMLInputChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.uuid


class ListCollaborationMLInputChannelsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channels that you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationMLInputChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationMLInputChannelsRequest:
    out: ListCollaborationMLInputChannelsRequest = {}  # type: ignore[typeddict-item]
    return out
