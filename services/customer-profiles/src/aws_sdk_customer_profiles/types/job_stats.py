"""Generated from Smithy shape ``com.amazonaws.customerprofiles#JobStats``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.long


class JobStats(TypedDict):
    number_of_profiles_reviewed: "aws_sdk_customer_profiles.types.long.long"
    """<p>The number of profiles reviewed.</p>"""
    number_of_matches_found: "aws_sdk_customer_profiles.types.long.long"
    """<p>The number of matches found.</p>"""
    number_of_merges_done: "aws_sdk_customer_profiles.types.long.long"
    """<p>The number of merges completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobStats) -> dict:
    out: dict = {}
    out["NumberOfProfilesReviewed"] = value.get("number_of_profiles_reviewed", 0)
    out["NumberOfMatchesFound"] = value.get("number_of_matches_found", 0)
    out["NumberOfMergesDone"] = value.get("number_of_merges_done", 0)
    return out


def deserialize_json(data: dict) -> JobStats:
    out: JobStats = {}  # type: ignore[typeddict-item]
    if "NumberOfProfilesReviewed" in data:
        out["number_of_profiles_reviewed"] = data["NumberOfProfilesReviewed"]
    else:
        out["number_of_profiles_reviewed"] = 0
    if "NumberOfMatchesFound" in data:
        out["number_of_matches_found"] = data["NumberOfMatchesFound"]
    else:
        out["number_of_matches_found"] = 0
    if "NumberOfMergesDone" in data:
        out["number_of_merges_done"] = data["NumberOfMergesDone"]
    else:
        out["number_of_merges_done"] = 0
    return out
