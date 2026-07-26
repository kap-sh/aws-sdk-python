"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.cis_finding_arn
    import capo_inspector2.types.cis_finding_status
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.resource_id


class CisScanResultDetails(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The CIS scan result details' scan ARN.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The CIS scan result details' account ID.</p>"""
    target_resource_id: NotRequired["capo_inspector2.types.resource_id.ResourceId"]
    """<p>The CIS scan result details' target resource ID.</p>"""
    platform: NotRequired["str"]
    """<p>The CIS scan result details' platform.</p>"""
    status: NotRequired["capo_inspector2.types.cis_finding_status.CisFindingStatus"]
    """<p>The CIS scan result details' status.</p>"""
    status_reason: NotRequired["str"]
    """<p>The CIS scan result details' status reason.</p>"""
    check_id: NotRequired["str"]
    """<p>The CIS scan result details' check ID.</p>"""
    title: NotRequired["str"]
    """<p>The CIS scan result details' title.</p>"""
    check_description: NotRequired["str"]
    """<p>The account ID that's associated with the CIS scan result details.</p>"""
    remediation: NotRequired["str"]
    """<p>The CIS scan result details' remediation.</p>"""
    level: NotRequired["capo_inspector2.types.cis_security_level.CisSecurityLevel"]
    """<p>The CIS scan result details' level.</p>"""
    finding_arn: NotRequired["capo_inspector2.types.cis_finding_arn.CisFindingArn"]
    """<p>The CIS scan result details' finding ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultDetails) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "target_resource_id" in value:
        out["targetResourceId"] = value["target_resource_id"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "status" in value:
        import capo_inspector2.types.cis_finding_status

        out["status"] = capo_inspector2.types.cis_finding_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "check_id" in value:
        out["checkId"] = value["check_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "check_description" in value:
        out["checkDescription"] = value["check_description"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    if "level" in value:
        import capo_inspector2.types.cis_security_level

        out["level"] = capo_inspector2.types.cis_security_level.serialize_json(
            value["level"]
        )
    if "finding_arn" in value:
        out["findingArn"] = value["finding_arn"]
    return out


def deserialize_json(data: dict) -> CisScanResultDetails:
    out: CisScanResultDetails = {}  # type: ignore[typeddict-item]
    if "scanArn" in data:
        out["scan_arn"] = data["scanArn"]
    else:
        raise DeserializationError("CisScanResultDetails.scan_arn required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "targetResourceId" in data:
        out["target_resource_id"] = data["targetResourceId"]
    if "platform" in data:
        out["platform"] = data["platform"]
    if "status" in data:
        import capo_inspector2.types.cis_finding_status

        out["status"] = capo_inspector2.types.cis_finding_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "checkId" in data:
        out["check_id"] = data["checkId"]
    if "title" in data:
        out["title"] = data["title"]
    if "checkDescription" in data:
        out["check_description"] = data["checkDescription"]
    if "remediation" in data:
        out["remediation"] = data["remediation"]
    if "level" in data:
        import capo_inspector2.types.cis_security_level

        out["level"] = capo_inspector2.types.cis_security_level.deserialize_json(
            data["level"]
        )
    if "findingArn" in data:
        out["finding_arn"] = data["findingArn"]
    return out
