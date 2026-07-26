"""Generated from Smithy shape ``com.amazonaws.inspector2#SendCisSessionHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.uuid


class SendCisSessionHealthRequest(TypedDict, closed=True):
    scan_job_id: "capo_inspector2.types.uuid.UUID"
    """<p>A unique identifier for the scan job.</p>"""
    session_token: "capo_inspector2.types.uuid.UUID"
    """<p>The unique token that identifies the CIS session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendCisSessionHealthRequest) -> dict:
    out: dict = {}
    out["scanJobId"] = value["scan_job_id"]
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_json(data: dict) -> SendCisSessionHealthRequest:
    out: SendCisSessionHealthRequest = {}  # type: ignore[typeddict-item]
    if "scanJobId" in data:
        out["scan_job_id"] = data["scanJobId"]
    else:
        raise DeserializationError("SendCisSessionHealthRequest.scan_job_id required")
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    else:
        raise DeserializationError("SendCisSessionHealthRequest.session_token required")
    return out
