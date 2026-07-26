"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DomainStats``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.long


class DomainStats(TypedDict, closed=True):
    profile_count: "capo_customer_profiles.types.long.long"
    """<p>The total number of profiles currently in the domain.</p>"""
    metering_profile_count: "capo_customer_profiles.types.long.long"
    """<p>The number of profiles that you are currently paying for in the domain. If you have more than 100 objects associated with a single profile, that profile counts as two profiles. If you have more than 200 objects, that profile counts as three, and so on.</p>"""
    object_count: "capo_customer_profiles.types.long.long"
    """<p>The total number of objects in domain.</p>"""
    total_size: "capo_customer_profiles.types.long.long"
    """<p>The total size, in bytes, of all objects in the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainStats) -> dict:
    out: dict = {}
    out["ProfileCount"] = value.get("profile_count", 0)
    out["MeteringProfileCount"] = value.get("metering_profile_count", 0)
    out["ObjectCount"] = value.get("object_count", 0)
    out["TotalSize"] = value.get("total_size", 0)
    return out


def deserialize_json(data: dict) -> DomainStats:
    out: DomainStats = {}  # type: ignore[typeddict-item]
    if "ProfileCount" in data:
        out["profile_count"] = data["ProfileCount"]
    else:
        out["profile_count"] = 0
    if "MeteringProfileCount" in data:
        out["metering_profile_count"] = data["MeteringProfileCount"]
    else:
        out["metering_profile_count"] = 0
    if "ObjectCount" in data:
        out["object_count"] = data["ObjectCount"]
    else:
        out["object_count"] = 0
    if "TotalSize" in data:
        out["total_size"] = data["TotalSize"]
    else:
        out["total_size"] = 0
    return out
