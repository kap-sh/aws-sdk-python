"""Generated from Smithy shape ``com.amazonaws.qconnect#ListMessagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_list
    import aws_sdk_qconnect.types.next_token


class ListMessagesResponse(TypedDict):
    messages: "aws_sdk_qconnect.types.message_list.MessageList"
    """<p>The message information.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessagesResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.message_list

    out["messages"] = aws_sdk_qconnect.types.message_list.serialize_json(
        value["messages"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMessagesResponse:
    out: ListMessagesResponse = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_qconnect.types.message_list

        out["messages"] = aws_sdk_qconnect.types.message_list.deserialize_json(
            data["messages"]
        )
    else:
        raise DeserializationError("ListMessagesResponse.messages required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
