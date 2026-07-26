"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorFeaturesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsGuardDutyDetectorFeaturesDetails(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Indicates the name of the feature that is activated for the detector. </p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Indicates the status of the feature that is activated for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorFeaturesDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorFeaturesDetails:
    out: AwsGuardDutyDetectorFeaturesDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
