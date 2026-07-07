"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.messages
    import aws_sdk_qbusiness.types.next_token


class ListMessagesResponse(TypedDict, closed=True):
    messages: NotRequired["aws_sdk_qbusiness.types.messages.Messages"]
    """<p>An array of information on one or more messages.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessagesResponse) -> dict:
    out: dict = {}
    if "messages" in value:
        import aws_sdk_qbusiness.types.messages

        out["messages"] = aws_sdk_qbusiness.types.messages.serialize_json(
            value["messages"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMessagesResponse:
    out: ListMessagesResponse = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_qbusiness.types.messages

        out["messages"] = aws_sdk_qbusiness.types.messages.deserialize_json(
            data["messages"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
