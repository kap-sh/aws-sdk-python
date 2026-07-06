"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.session_id


class GetSessionRequest(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application that the session belongs to.</p>"""
    session_id: "aws_sdk_emr_serverless.types.session_id.SessionId"
    """<p>The ID of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionRequest:
    out: GetSessionRequest = {}  # type: ignore[typeddict-item]
    return out
