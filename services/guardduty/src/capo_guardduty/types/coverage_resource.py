"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.coverage_resource_details
    import capo_guardduty.types.coverage_status
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class CoverageResource(TypedDict, closed=True):
    resource_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID of the resource.</p>"""
    detector_id: NotRequired["capo_guardduty.types.detector_id.DetectorId"]
    """<p>The unique ID of the GuardDuty detector associated with the resource.</p>"""
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The unique ID of the Amazon Web Services account.</p>"""
    resource_details: NotRequired[
        "capo_guardduty.types.coverage_resource_details.CoverageResourceDetails"
    ]
    """<p>Information about the resource for which the coverage statistics are retrieved.</p>"""
    coverage_status: NotRequired["capo_guardduty.types.coverage_status.CoverageStatus"]
    """<p>Represents the status of the EKS cluster coverage.</p>"""
    issue: NotRequired["capo_guardduty.types.string.String"]
    """<p>Represents the reason why a coverage status was <code>UNHEALTHY</code> for the EKS cluster.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the coverage details for the resource were last updated. This is in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageResource) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "resource_details" in value:
        import capo_guardduty.types.coverage_resource_details

        out["resourceDetails"] = (
            capo_guardduty.types.coverage_resource_details.serialize_json(
                value["resource_details"]
            )
        )
    if "coverage_status" in value:
        import capo_guardduty.types.coverage_status

        out["coverageStatus"] = capo_guardduty.types.coverage_status.serialize_json(
            value["coverage_status"]
        )
    if "issue" in value:
        out["issue"] = value["issue"]
    if "updated_at" in value:
        import capo_guardduty.types.timestamp

        out["updatedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CoverageResource:
    out: CoverageResource = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "resourceDetails" in data:
        import capo_guardduty.types.coverage_resource_details

        out["resource_details"] = (
            capo_guardduty.types.coverage_resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    if "coverageStatus" in data:
        import capo_guardduty.types.coverage_status

        out["coverage_status"] = capo_guardduty.types.coverage_status.deserialize_json(
            data["coverageStatus"]
        )
    if "issue" in data:
        out["issue"] = data["issue"]
    if "updatedAt" in data:
        import capo_guardduty.types.timestamp

        out["updated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
