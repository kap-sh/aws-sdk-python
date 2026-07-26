"""Generated from Smithy shape ``com.amazonaws.iotdataplane#ListRetainedMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.next_token
    import capo_iot_data_plane.types.retained_message_list


class ListRetainedMessagesResponse(TypedDict, closed=True):
    retained_topics: NotRequired[
        "capo_iot_data_plane.types.retained_message_list.RetainedMessageList"
    ]
    """<p>A summary list the account's retained messages. The information returned doesn't include the message payloads of the retained messages.</p>"""
    next_token: NotRequired["capo_iot_data_plane.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetainedMessagesResponse) -> dict:
    out: dict = {}
    if "retained_topics" in value:
        import capo_iot_data_plane.types.retained_message_list

        out["retainedTopics"] = (
            capo_iot_data_plane.types.retained_message_list.serialize_json(
                value["retained_topics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetainedMessagesResponse:
    out: ListRetainedMessagesResponse = {}  # type: ignore[typeddict-item]
    if "retainedTopics" in data:
        import capo_iot_data_plane.types.retained_message_list

        out["retained_topics"] = (
            capo_iot_data_plane.types.retained_message_list.deserialize_json(
                data["retainedTopics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
