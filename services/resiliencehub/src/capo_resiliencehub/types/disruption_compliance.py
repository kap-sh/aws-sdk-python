"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DisruptionCompliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.seconds
    import capo_resiliencehub.types.string500


class DisruptionCompliance(TypedDict, closed=True):
    achievable_rto_in_secs: "capo_resiliencehub.types.seconds.Seconds"
    """<p>The Recovery Time Objective (RTO) that is achievable, in seconds</p>"""
    current_rto_in_secs: "capo_resiliencehub.types.seconds.Seconds"
    """<p>The current RTO, in seconds.</p>"""
    rto_reference_id: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Reference identifier of the RTO.</p>"""
    rto_description: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The RTO description.</p>"""
    current_rpo_in_secs: "capo_resiliencehub.types.seconds.Seconds"
    """<p>The current RPO, in seconds.</p>"""
    rpo_reference_id: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Reference identifier of the RPO .</p>"""
    rpo_description: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The RPO description.</p>"""
    compliance_status: "capo_resiliencehub.types.compliance_status.ComplianceStatus"
    """<p>The current status of compliance for the resiliency policy.</p>"""
    achievable_rpo_in_secs: "capo_resiliencehub.types.seconds.Seconds"
    """<p>The Recovery Point Objective (RPO) that is achievable, in seconds.</p>"""
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The disruption compliance message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisruptionCompliance) -> dict:
    out: dict = {}
    out["achievableRtoInSecs"] = value.get("achievable_rto_in_secs", 0)
    out["currentRtoInSecs"] = value.get("current_rto_in_secs", 0)
    if "rto_reference_id" in value:
        out["rtoReferenceId"] = value["rto_reference_id"]
    if "rto_description" in value:
        out["rtoDescription"] = value["rto_description"]
    out["currentRpoInSecs"] = value.get("current_rpo_in_secs", 0)
    if "rpo_reference_id" in value:
        out["rpoReferenceId"] = value["rpo_reference_id"]
    if "rpo_description" in value:
        out["rpoDescription"] = value["rpo_description"]
    import capo_resiliencehub.types.compliance_status

    out["complianceStatus"] = capo_resiliencehub.types.compliance_status.serialize_json(
        value["compliance_status"]
    )
    out["achievableRpoInSecs"] = value.get("achievable_rpo_in_secs", 0)
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DisruptionCompliance:
    out: DisruptionCompliance = {}  # type: ignore[typeddict-item]
    if "achievableRtoInSecs" in data:
        out["achievable_rto_in_secs"] = data["achievableRtoInSecs"]
    else:
        out["achievable_rto_in_secs"] = 0
    if "currentRtoInSecs" in data:
        out["current_rto_in_secs"] = data["currentRtoInSecs"]
    else:
        out["current_rto_in_secs"] = 0
    if "rtoReferenceId" in data:
        out["rto_reference_id"] = data["rtoReferenceId"]
    if "rtoDescription" in data:
        out["rto_description"] = data["rtoDescription"]
    if "currentRpoInSecs" in data:
        out["current_rpo_in_secs"] = data["currentRpoInSecs"]
    else:
        out["current_rpo_in_secs"] = 0
    if "rpoReferenceId" in data:
        out["rpo_reference_id"] = data["rpoReferenceId"]
    if "rpoDescription" in data:
        out["rpo_description"] = data["rpoDescription"]
    if "complianceStatus" in data:
        import capo_resiliencehub.types.compliance_status

        out["compliance_status"] = (
            capo_resiliencehub.types.compliance_status.deserialize_json(
                data["complianceStatus"]
            )
        )
    else:
        raise DeserializationError("DisruptionCompliance.compliance_status required")
    if "achievableRpoInSecs" in data:
        out["achievable_rpo_in_secs"] = data["achievableRpoInSecs"]
    else:
        out["achievable_rpo_in_secs"] = 0
    if "message" in data:
        out["message"] = data["message"]
    return out
