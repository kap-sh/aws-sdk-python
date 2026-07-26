"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListChatResponseConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_response_configurations
    import capo_qbusiness.types.next_token


class ListChatResponseConfigurationsResponse(TypedDict, closed=True):
    chat_response_configurations: NotRequired[
        "capo_qbusiness.types.chat_response_configurations.ChatResponseConfigurations"
    ]
    """<p>A list of chat response configuration summaries, each containing key information about an available configuration in the specified application.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>A pagination token that can be used in a subsequent request to retrieve additional chat response configurations if the results were truncated due to the <code>maxResults</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChatResponseConfigurationsResponse) -> dict:
    out: dict = {}
    if "chat_response_configurations" in value:
        import capo_qbusiness.types.chat_response_configurations

        out["chatResponseConfigurations"] = (
            capo_qbusiness.types.chat_response_configurations.serialize_json(
                value["chat_response_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChatResponseConfigurationsResponse:
    out: ListChatResponseConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "chatResponseConfigurations" in data:
        import capo_qbusiness.types.chat_response_configurations

        out["chat_response_configurations"] = (
            capo_qbusiness.types.chat_response_configurations.deserialize_json(
                data["chatResponseConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
