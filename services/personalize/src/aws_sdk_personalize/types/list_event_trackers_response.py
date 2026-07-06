"""Generated from Smithy shape ``com.amazonaws.personalize#ListEventTrackersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.event_trackers
    import aws_sdk_personalize.types.next_token


class ListEventTrackersResponse(TypedDict, closed=True):
    event_trackers: NotRequired[
        "aws_sdk_personalize.types.event_trackers.EventTrackers"
    ]
    """<p>A list of event trackers.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of event trackers (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventTrackersResponse) -> dict:
    out: dict = {}
    if "event_trackers" in value:
        import aws_sdk_personalize.types.event_trackers

        out["eventTrackers"] = (
            aws_sdk_personalize.types.event_trackers.serialize_aws_json_1_1(
                value["event_trackers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventTrackersResponse:
    out: ListEventTrackersResponse = {}  # type: ignore[typeddict-item]
    if "eventTrackers" in data:
        import aws_sdk_personalize.types.event_trackers

        out["event_trackers"] = (
            aws_sdk_personalize.types.event_trackers.deserialize_aws_json_1_1(
                data["eventTrackers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
