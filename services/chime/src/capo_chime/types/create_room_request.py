"""Generated from Smithy shape ``com.amazonaws.chime#CreateRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.client_request_token
    import capo_chime.types.non_empty_string
    import capo_chime.types.sensitive_string


class CreateRoomRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    name: "capo_chime.types.sensitive_string.SensitiveString"
    """<p>The room name.</p>"""
    client_request_token: NotRequired[
        "capo_chime.types.client_request_token.ClientRequestToken"
    ]
    """<p>The idempotency token for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateRoomRequest:
    out: CreateRoomRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRoomRequest.name required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
