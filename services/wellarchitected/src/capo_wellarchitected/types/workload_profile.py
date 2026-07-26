"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.profile_version


class WorkloadProfile(TypedDict, closed=True):
    profile_arn: NotRequired["capo_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    profile_version: NotRequired[
        "capo_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The profile version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadProfile) -> dict:
    out: dict = {}
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "profile_version" in value:
        out["ProfileVersion"] = value["profile_version"]
    return out


def deserialize_json(data: dict) -> WorkloadProfile:
    out: WorkloadProfile = {}  # type: ignore[typeddict-item]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "ProfileVersion" in data:
        out["profile_version"] = data["ProfileVersion"]
    return out
