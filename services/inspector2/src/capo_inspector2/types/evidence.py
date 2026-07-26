"""Generated from Smithy shape ``com.amazonaws.inspector2#Evidence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.evidence_detail
    import capo_inspector2.types.evidence_rule
    import capo_inspector2.types.evidence_severity


class Evidence(TypedDict, closed=True):
    evidence_rule: NotRequired["capo_inspector2.types.evidence_rule.EvidenceRule"]
    """<p>The evidence rule.</p>"""
    evidence_detail: NotRequired["capo_inspector2.types.evidence_detail.EvidenceDetail"]
    """<p>The evidence details.</p>"""
    severity: NotRequired["capo_inspector2.types.evidence_severity.EvidenceSeverity"]
    """<p>The evidence severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evidence) -> dict:
    out: dict = {}
    if "evidence_rule" in value:
        out["evidenceRule"] = value["evidence_rule"]
    if "evidence_detail" in value:
        out["evidenceDetail"] = value["evidence_detail"]
    if "severity" in value:
        out["severity"] = value["severity"]
    return out


def deserialize_json(data: dict) -> Evidence:
    out: Evidence = {}  # type: ignore[typeddict-item]
    if "evidenceRule" in data:
        out["evidence_rule"] = data["evidenceRule"]
    if "evidenceDetail" in data:
        out["evidence_detail"] = data["evidenceDetail"]
    if "severity" in data:
        out["severity"] = data["severity"]
    return out
