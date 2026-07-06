"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetTranscriptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.contact_id
    import aws_sdk_connectparticipant.types.next_token
    import aws_sdk_connectparticipant.types.transcript


class GetTranscriptResponse(TypedDict, closed=True):
    initial_contact_id: NotRequired[
        "aws_sdk_connectparticipant.types.contact_id.ContactId"
    ]
    """<p>The initial contact ID for the contact. </p>"""
    transcript: NotRequired["aws_sdk_connectparticipant.types.transcript.Transcript"]
    """<p>The list of messages in the session.</p>"""
    next_token: NotRequired["aws_sdk_connectparticipant.types.next_token.NextToken"]
    """<p>The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTranscriptResponse) -> dict:
    out: dict = {}
    if "initial_contact_id" in value:
        out["InitialContactId"] = value["initial_contact_id"]
    if "transcript" in value:
        import aws_sdk_connectparticipant.types.transcript

        out["Transcript"] = aws_sdk_connectparticipant.types.transcript.serialize_json(
            value["transcript"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTranscriptResponse:
    out: GetTranscriptResponse = {}  # type: ignore[typeddict-item]
    if "InitialContactId" in data:
        out["initial_contact_id"] = data["InitialContactId"]
    if "Transcript" in data:
        import aws_sdk_connectparticipant.types.transcript

        out["transcript"] = (
            aws_sdk_connectparticipant.types.transcript.deserialize_json(
                data["Transcript"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
