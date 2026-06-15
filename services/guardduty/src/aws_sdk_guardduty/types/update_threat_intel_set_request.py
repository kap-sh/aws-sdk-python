"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateThreatIntelSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.location
    import aws_sdk_guardduty.types.name
    import aws_sdk_guardduty.types.string


class UpdateThreatIntelSetRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    threat_intel_set_id: "aws_sdk_guardduty.types.string.String"
    """<p>The unique ID that specifies the ThreatIntelSet that you want to update.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.name.Name"]
    """<p>The unique ID that specifies the ThreatIntelSet that you want to update.</p>"""
    location: NotRequired["aws_sdk_guardduty.types.location.Location"]
    """<p>The updated URI of the file that contains the ThreateIntelSet.</p>"""
    activate: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>The updated Boolean value that specifies whether the ThreateIntelSet is active or not.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThreatIntelSetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "location" in value:
        out["location"] = value["location"]
    if "activate" in value:
        out["activate"] = value["activate"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> UpdateThreatIntelSetRequest:
    out: UpdateThreatIntelSetRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "location" in data:
        out["location"] = data["location"]
    if "activate" in data:
        out["activate"] = data["activate"]
    if "expectedBucketOwner" in data:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out
