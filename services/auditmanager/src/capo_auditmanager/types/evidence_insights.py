"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceInsights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.nullable_integer


class EvidenceInsights(TypedDict, closed=True):
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
    """<p>The number of evidence that a compliance check ruling isn't available for. Evidence is inconclusive when the associated control uses Security Hub CSPM or Config as a data source but you didn't enable those services. This is also the case when a control uses a data source that doesn’t support compliance checks (for example, manual evidence, API calls, or CloudTrail). </p> <note> <p>If evidence has a compliance check status of <i>not applicable</i> in the console, it's classified as <i>inconclusive</i> in <code>EvidenceInsights</code> data.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceInsights) -> dict:
    out: dict = {}
    if "noncompliant_evidence_count" in value:
        out["noncompliantEvidenceCount"] = value["noncompliant_evidence_count"]
    if "compliant_evidence_count" in value:
        out["compliantEvidenceCount"] = value["compliant_evidence_count"]
    if "inconclusive_evidence_count" in value:
        out["inconclusiveEvidenceCount"] = value["inconclusive_evidence_count"]
    return out


def deserialize_json(data: dict) -> EvidenceInsights:
    out: EvidenceInsights = {}  # type: ignore[typeddict-item]
    if "noncompliantEvidenceCount" in data:
        out["noncompliant_evidence_count"] = data["noncompliantEvidenceCount"]
    if "compliantEvidenceCount" in data:
        out["compliant_evidence_count"] = data["compliantEvidenceCount"]
    if "inconclusiveEvidenceCount" in data:
        out["inconclusive_evidence_count"] = data["inconclusiveEvidenceCount"]
    return out
