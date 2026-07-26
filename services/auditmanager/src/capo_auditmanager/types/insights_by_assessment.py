"""Generated from Smithy shape ``com.amazonaws.auditmanager#InsightsByAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.nullable_integer
    import capo_auditmanager.types.timestamp


class InsightsByAssessment(TypedDict, closed=True):
    noncompliant_evidence_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of compliance check evidence that Audit Manager classified as non-compliant. This includes evidence that was collected from Security Hub CSPM with a <i>Fail</i> ruling, or collected from Config with a <i>Non-compliant</i> ruling. </p>"""
    compliant_evidence_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of compliance check evidence that Audit Manager classified as compliant. This includes evidence that was collected from Security Hub CSPM with a <i>Pass</i> ruling, or collected from Config with a <i>Compliant</i> ruling. </p>"""
    inconclusive_evidence_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The amount of evidence without a compliance check ruling. Evidence is inconclusive if the associated control uses Security Hub CSPM or Config as a data source and you didn't enable those services. This is also the case if a control uses a data source that doesn’t support compliance checks (for example, manual evidence, API calls, or CloudTrail). </p> <note> <p>If evidence has a compliance check status of <i>not applicable</i>, it's classified as <i>inconclusive</i> in <code>InsightsByAssessment</code> data.</p> </note>"""
    assessment_controls_count_by_noncompliant_evidence: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of assessment controls that collected non-compliant evidence on the <code>lastUpdated</code> date. </p>"""
    total_assessment_controls_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The total number of controls in the assessment. </p>"""
    last_updated: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p>The time when the assessment insights were last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsByAssessment) -> dict:
    out: dict = {}
    if "noncompliant_evidence_count" in value:
        out["noncompliantEvidenceCount"] = value["noncompliant_evidence_count"]
    if "compliant_evidence_count" in value:
        out["compliantEvidenceCount"] = value["compliant_evidence_count"]
    if "inconclusive_evidence_count" in value:
        out["inconclusiveEvidenceCount"] = value["inconclusive_evidence_count"]
    if "assessment_controls_count_by_noncompliant_evidence" in value:
        out["assessmentControlsCountByNoncompliantEvidence"] = value[
            "assessment_controls_count_by_noncompliant_evidence"
        ]
    if "total_assessment_controls_count" in value:
        out["totalAssessmentControlsCount"] = value["total_assessment_controls_count"]
    if "last_updated" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdated"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    return out


def deserialize_json(data: dict) -> InsightsByAssessment:
    out: InsightsByAssessment = {}  # type: ignore[typeddict-item]
    if "noncompliantEvidenceCount" in data:
        out["noncompliant_evidence_count"] = data["noncompliantEvidenceCount"]
    if "compliantEvidenceCount" in data:
        out["compliant_evidence_count"] = data["compliantEvidenceCount"]
    if "inconclusiveEvidenceCount" in data:
        out["inconclusive_evidence_count"] = data["inconclusiveEvidenceCount"]
    if "assessmentControlsCountByNoncompliantEvidence" in data:
        out["assessment_controls_count_by_noncompliant_evidence"] = data[
            "assessmentControlsCountByNoncompliantEvidence"
        ]
    if "totalAssessmentControlsCount" in data:
        out["total_assessment_controls_count"] = data["totalAssessmentControlsCount"]
    if "lastUpdated" in data:
        import capo_auditmanager.types.timestamp

        out["last_updated"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    return out
