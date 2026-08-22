"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SessionConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class SessionConfiguration(TypedDict, closed=True):
    session_timeout_in_seconds: NotRequired["int"]
    """<p>The session timeout in seconds. After this timeout, the session expires and subsequent requests to this session will receive an error. The minimum value is 900 seconds (15 minutes), the maximum value is 28800 seconds (8 hours), and the default value is 3600 seconds (1 hour).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionConfiguration) -> dict:
    out: dict = {}
    if "session_timeout_in_seconds" in value:
        out["sessionTimeoutInSeconds"] = value["session_timeout_in_seconds"]
    return out


def deserialize_json(data: dict) -> SessionConfiguration:
    out: SessionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sessionTimeoutInSeconds") is not None:
        out["session_timeout_in_seconds"] = data["sessionTimeoutInSeconds"]
    return out
