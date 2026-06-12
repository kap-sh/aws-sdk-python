"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListQueuedMessagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.downlink_queue_messages_list
    import aws_sdk_iot_wireless.types.next_token


class ListQueuedMessagesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    downlink_queue_messages_list: NotRequired[
        "aws_sdk_iot_wireless.types.downlink_queue_messages_list.DownlinkQueueMessagesList"
    ]
    """<p>The messages in the downlink queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuedMessagesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "downlink_queue_messages_list" in value:
        import aws_sdk_iot_wireless.types.downlink_queue_messages_list

        out["DownlinkQueueMessagesList"] = (
            aws_sdk_iot_wireless.types.downlink_queue_messages_list.serialize_json(
                value["downlink_queue_messages_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListQueuedMessagesResponse:
    out: ListQueuedMessagesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DownlinkQueueMessagesList" in data:
        import aws_sdk_iot_wireless.types.downlink_queue_messages_list

        out["downlink_queue_messages_list"] = (
            aws_sdk_iot_wireless.types.downlink_queue_messages_list.deserialize_json(
                data["DownlinkQueueMessagesList"]
            )
        )
    return out
