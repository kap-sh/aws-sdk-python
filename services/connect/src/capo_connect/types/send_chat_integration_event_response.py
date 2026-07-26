"""Generated from Smithy shape ``com.amazonaws.connect#SendChatIntegrationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.new_chat_created


class SendChatIntegrationEventResponse(TypedDict, closed=True):
    initial_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>Identifier of chat contact used to handle integration event. This may be null if the integration event is not valid without an already existing chat contact.</p>"""
    new_chat_created: NotRequired["capo_connect.types.new_chat_created.NewChatCreated"]
    """<p>Whether handling the integration event resulted in creating a new chat or acting on existing chat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendChatIntegrationEventResponse) -> dict:
    out: dict = {}
    if "initial_contact_id" in value:
        out["InitialContactId"] = value["initial_contact_id"]
    if "new_chat_created" in value:
        out["NewChatCreated"] = value["new_chat_created"]
    return out


def deserialize_json(data: dict) -> SendChatIntegrationEventResponse:
    out: SendChatIntegrationEventResponse = {}  # type: ignore[typeddict-item]
    if "InitialContactId" in data:
        out["initial_contact_id"] = data["InitialContactId"]
    if "NewChatCreated" in data:
        out["new_chat_created"] = data["NewChatCreated"]
    return out
