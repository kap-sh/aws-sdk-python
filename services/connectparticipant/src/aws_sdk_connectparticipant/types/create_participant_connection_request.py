"""Generated from Smithy shape ``com.amazonaws.connectparticipant#CreateParticipantConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.bool
    import aws_sdk_connectparticipant.types.connection_type_list
    import aws_sdk_connectparticipant.types.participant_token


class CreateParticipantConnectionRequest(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_connectparticipant.types.connection_type_list.ConnectionTypeList"
    ]
    """<p>Type of connection information required. If you need <code>CONNECTION_CREDENTIALS</code> along with marking participant as connected, pass <code>CONNECTION_CREDENTIALS</code> in <code>Type</code>.</p>"""
    participant_token: (
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    )
    r"""<p>This is a header parameter.</p> <p>The ParticipantToken as obtained from <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html\">StartChatContact</a> API response.</p>"""
    connect_participant: NotRequired["aws_sdk_connectparticipant.types.bool.Bool"]
    """<p>Amazon Connect Participant is used to mark the participant as connected for customer participant in message streaming, as well as for agent or manager participant in non-streaming chats.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantConnectionRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_connectparticipant.types.connection_type_list

        out["Type"] = (
            aws_sdk_connectparticipant.types.connection_type_list.serialize_json(
                value["type"]
            )
        )
    if "connect_participant" in value:
        out["ConnectParticipant"] = value["connect_participant"]
    return out


def deserialize_json(data: dict) -> CreateParticipantConnectionRequest:
    out: CreateParticipantConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connectparticipant.types.connection_type_list

        out["type"] = (
            aws_sdk_connectparticipant.types.connection_type_list.deserialize_json(
                data["Type"]
            )
        )
    if "ConnectParticipant" in data:
        out["connect_participant"] = data["ConnectParticipant"]
    return out
