"""Generated from Smithy shape ``com.amazonaws.iotdataplane#ListRetainedMessagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.next_token
    import aws_sdk_iot_data_plane.types.retained_message_list


class ListRetainedMessagesResponse(TypedDict):
    retained_topics: NotRequired[
        "aws_sdk_iot_data_plane.types.retained_message_list.RetainedMessageList"
    ]
    """<p>A summary list the account's retained messages. The information returned doesn't include the message payloads of the retained messages.</p>"""
    next_token: NotRequired["aws_sdk_iot_data_plane.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetainedMessagesResponse) -> dict:
    out: dict = {}
    if "retained_topics" in value:
        import aws_sdk_iot_data_plane.types.retained_message_list

        out["retainedTopics"] = (
            aws_sdk_iot_data_plane.types.retained_message_list.serialize_json(
                value["retained_topics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetainedMessagesResponse:
    out: ListRetainedMessagesResponse = {}  # type: ignore[typeddict-item]
    if "retainedTopics" in data:
        import aws_sdk_iot_data_plane.types.retained_message_list

        out["retained_topics"] = (
            aws_sdk_iot_data_plane.types.retained_message_list.deserialize_json(
                data["retainedTopics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
