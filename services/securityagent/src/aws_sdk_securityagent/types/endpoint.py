"""Generated from Smithy shape ``com.amazonaws.securityagent#Endpoint``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Endpoint(TypedDict):
    uri: NotRequired["str"]
    """<p>The URI of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Endpoint) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    return out
