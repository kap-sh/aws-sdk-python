"""Generated from Smithy shape ``com.amazonaws.proton#ResourceCountsSummary``."""

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError


class ResourceCountsSummary(TypedDict, closed=True):
    total: "int"
    """<p>The total number of resources of this type in the Amazon Web Services account.</p>"""
    failed: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that failed to deploy.</p>"""
    up_to_date: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.</p>"""
    behind_major: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that need a major template version update.</p>"""
    behind_minor: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that need a minor template version update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceCountsSummary) -> dict:
    out: dict = {}
    out["total"] = value["total"]
    if "failed" in value:
        out["failed"] = value["failed"]
    if "up_to_date" in value:
        out["upToDate"] = value["up_to_date"]
    if "behind_major" in value:
        out["behindMajor"] = value["behind_major"]
    if "behind_minor" in value:
        out["behindMinor"] = value["behind_minor"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceCountsSummary:
    out: ResourceCountsSummary = {}  # type: ignore[typeddict-item]
    if "total" in data:
        out["total"] = data["total"]
    else:
        raise DeserializationError("ResourceCountsSummary.total required")
    if "failed" in data:
        out["failed"] = data["failed"]
    if "upToDate" in data:
        out["up_to_date"] = data["upToDate"]
    if "behindMajor" in data:
        out["behind_major"] = data["behindMajor"]
    if "behindMinor" in data:
        out["behind_minor"] = data["behindMinor"]
    return out
