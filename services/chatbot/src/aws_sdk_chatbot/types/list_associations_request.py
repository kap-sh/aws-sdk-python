"""Generated from Smithy shape ``com.amazonaws.chatbot#ListAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.string


class ListAssociationsRequest(TypedDict):
    chat_configuration: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The channel configuration to list associations for.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_chatbot.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociationsRequest) -> dict:
    out: dict = {}
    out["ChatConfiguration"] = value["chat_configuration"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociationsRequest:
    out: ListAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfiguration" in data:
        out["chat_configuration"] = data["ChatConfiguration"]
    else:
        raise DeserializationError(
            "ListAssociationsRequest.chat_configuration required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
