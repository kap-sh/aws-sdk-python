"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAgentResponse``."""

from typing_extensions import NotRequired, TypedDict


class DeleteAgentResponse(TypedDict, closed=True):
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteAgentResponse:
    out: DeleteAgentResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
