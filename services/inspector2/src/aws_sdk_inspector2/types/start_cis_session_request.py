"""Generated from Smithy shape ``com.amazonaws.inspector2#StartCisSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.start_cis_session_message
    import aws_sdk_inspector2.types.uuid


class StartCisSessionRequest(TypedDict):
    scan_job_id: "aws_sdk_inspector2.types.uuid.UUID"
    """<p>A unique identifier for the scan job.</p>"""
    message: "aws_sdk_inspector2.types.start_cis_session_message.StartCisSessionMessage"
    """<p>The start CIS session message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCisSessionRequest) -> dict:
    out: dict = {}
    out["scanJobId"] = value["scan_job_id"]
    import aws_sdk_inspector2.types.start_cis_session_message

    out["message"] = aws_sdk_inspector2.types.start_cis_session_message.serialize_json(
        value["message"]
    )
    return out


def deserialize_json(data: dict) -> StartCisSessionRequest:
    out: StartCisSessionRequest = {}  # type: ignore[typeddict-item]
    if "scanJobId" in data:
        out["scan_job_id"] = data["scanJobId"]
    else:
        raise DeserializationError("StartCisSessionRequest.scan_job_id required")
    if "message" in data:
        import aws_sdk_inspector2.types.start_cis_session_message

        out["message"] = (
            aws_sdk_inspector2.types.start_cis_session_message.deserialize_json(
                data["message"]
            )
        )
    else:
        raise DeserializationError("StartCisSessionRequest.message required")
    return out
