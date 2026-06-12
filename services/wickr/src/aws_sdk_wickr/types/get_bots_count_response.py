"""Generated from Smithy shape ``com.amazonaws.wickr#GetBotsCountResponse``."""

from typing import TypedDict

from aws_sdk_wickr.errors import DeserializationError


class GetBotsCountResponse(TypedDict):
    pending: "int"
    """<p>The number of bots with pending status (invited but not yet activated).</p>"""
    active: "int"
    """<p>The number of bots with active status.</p>"""
    total: "int"
    """<p>The total number of bots in the network (active and pending).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotsCountResponse) -> dict:
    out: dict = {}
    out["pending"] = value["pending"]
    out["active"] = value["active"]
    out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> GetBotsCountResponse:
    out: GetBotsCountResponse = {}  # type: ignore[typeddict-item]
    if "pending" in data:
        out["pending"] = data["pending"]
    else:
        raise DeserializationError("GetBotsCountResponse.pending required")
    if "active" in data:
        out["active"] = data["active"]
    else:
        raise DeserializationError("GetBotsCountResponse.active required")
    if "total" in data:
        out["total"] = data["total"]
    else:
        raise DeserializationError("GetBotsCountResponse.total required")
    return out
