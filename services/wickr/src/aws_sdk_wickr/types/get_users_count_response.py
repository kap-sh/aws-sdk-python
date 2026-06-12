"""Generated from Smithy shape ``com.amazonaws.wickr#GetUsersCountResponse``."""

from typing import TypedDict

from aws_sdk_wickr.errors import DeserializationError


class GetUsersCountResponse(TypedDict):
    pending: "int"
    """<p>The number of users with pending status (invited but not yet accepted).</p>"""
    active: "int"
    """<p>The number of users with active status in the network.</p>"""
    rejected: "int"
    """<p>The number of users who have rejected network invitations.</p>"""
    remaining: "int"
    """<p>The number of additional users that can be added to the network while maintaining premium free trial eligibility.</p>"""
    total: "int"
    """<p>The total number of users in the network (active and pending combined).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsersCountResponse) -> dict:
    out: dict = {}
    out["pending"] = value["pending"]
    out["active"] = value["active"]
    out["rejected"] = value["rejected"]
    out["remaining"] = value["remaining"]
    out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> GetUsersCountResponse:
    out: GetUsersCountResponse = {}  # type: ignore[typeddict-item]
    if "pending" in data:
        out["pending"] = data["pending"]
    else:
        raise DeserializationError("GetUsersCountResponse.pending required")
    if "active" in data:
        out["active"] = data["active"]
    else:
        raise DeserializationError("GetUsersCountResponse.active required")
    if "rejected" in data:
        out["rejected"] = data["rejected"]
    else:
        raise DeserializationError("GetUsersCountResponse.rejected required")
    if "remaining" in data:
        out["remaining"] = data["remaining"]
    else:
        raise DeserializationError("GetUsersCountResponse.remaining required")
    if "total" in data:
        out["total"] = data["total"]
    else:
        raise DeserializationError("GetUsersCountResponse.total required")
    return out
