"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTokenCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.iso8601_datetime
    import aws_sdk_connect.types.participant_token


class ParticipantTokenCredentials(TypedDict, closed=True):
    participant_token: NotRequired[
        "aws_sdk_connect.types.participant_token.ParticipantToken"
    ]
    r"""<p>The token used by the chat participant to call <a href=\"https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html\">CreateParticipantConnection</a>. The participant token is valid for the lifetime of a chat participant. </p>"""
    expiry: NotRequired["aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The expiration of the token. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenCredentials) -> dict:
    out: dict = {}
    if "participant_token" in value:
        out["ParticipantToken"] = value["participant_token"]
    if "expiry" in value:
        out["Expiry"] = value["expiry"]
    return out


def deserialize_json(data: dict) -> ParticipantTokenCredentials:
    out: ParticipantTokenCredentials = {}  # type: ignore[typeddict-item]
    if "ParticipantToken" in data:
        out["participant_token"] = data["ParticipantToken"]
    if "Expiry" in data:
        out["expiry"] = data["Expiry"]
    return out
