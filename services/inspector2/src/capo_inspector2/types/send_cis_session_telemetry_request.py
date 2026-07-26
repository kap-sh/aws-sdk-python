"""Generated from Smithy shape ``com.amazonaws.inspector2#SendCisSessionTelemetryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.cis_session_messages
    import capo_inspector2.types.uuid


class SendCisSessionTelemetryRequest(TypedDict, closed=True):
    scan_job_id: "capo_inspector2.types.uuid.UUID"
    """<p>A unique identifier for the scan job.</p>"""
    session_token: "capo_inspector2.types.uuid.UUID"
    """<p>The unique token that identifies the CIS session.</p>"""
    messages: "capo_inspector2.types.cis_session_messages.CisSessionMessages"
    """<p>The CIS session telemetry messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendCisSessionTelemetryRequest) -> dict:
    out: dict = {}
    out["scanJobId"] = value["scan_job_id"]
    out["sessionToken"] = value["session_token"]
    import capo_inspector2.types.cis_session_messages

    out["messages"] = capo_inspector2.types.cis_session_messages.serialize_json(
        value["messages"]
    )
    return out


def deserialize_json(data: dict) -> SendCisSessionTelemetryRequest:
    out: SendCisSessionTelemetryRequest = {}  # type: ignore[typeddict-item]
    if "scanJobId" in data:
        out["scan_job_id"] = data["scanJobId"]
    else:
        raise DeserializationError(
            "SendCisSessionTelemetryRequest.scan_job_id required"
        )
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    else:
        raise DeserializationError(
            "SendCisSessionTelemetryRequest.session_token required"
        )
    if "messages" in data:
        import capo_inspector2.types.cis_session_messages

        out["messages"] = capo_inspector2.types.cis_session_messages.deserialize_json(
            data["messages"]
        )
    else:
        raise DeserializationError("SendCisSessionTelemetryRequest.messages required")
    return out
