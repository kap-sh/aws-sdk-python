"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ResourceTypeDetails``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ResourceTypeDetails(TypedDict):
    total_active_public: NotRequired["int"]
    """<p>The total number of active public findings for the resource type.</p>"""
    total_active_cross_account: NotRequired["int"]
    """<p>The total number of active cross-account findings for the resource type.</p>"""
    total_active_errors: NotRequired["int"]
    """<p>The total number of active errors for the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeDetails) -> dict:
    out: dict = {}
    if "total_active_public" in value:
        out["totalActivePublic"] = value["total_active_public"]
    if "total_active_cross_account" in value:
        out["totalActiveCrossAccount"] = value["total_active_cross_account"]
    if "total_active_errors" in value:
        out["totalActiveErrors"] = value["total_active_errors"]
    return out


def deserialize_json(data: dict) -> ResourceTypeDetails:
    out: ResourceTypeDetails = {}  # type: ignore[typeddict-item]
    if "totalActivePublic" in data:
        out["total_active_public"] = data["totalActivePublic"]
    if "totalActiveCrossAccount" in data:
        out["total_active_cross_account"] = data["totalActiveCrossAccount"]
    if "totalActiveErrors" in data:
        out["total_active_errors"] = data["totalActiveErrors"]
    return out
