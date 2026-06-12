"""Generated from Smithy shape ``com.amazonaws.connectparticipant#DisconnectParticipantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.client_token
    import aws_sdk_connectparticipant.types.participant_token


class DisconnectParticipantRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_connectparticipant.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    connection_token: (
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    )
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectParticipantRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisconnectParticipantRequest:
    out: DisconnectParticipantRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
