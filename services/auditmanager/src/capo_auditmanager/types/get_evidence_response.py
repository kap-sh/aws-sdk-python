"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.evidence


class GetEvidenceResponse(TypedDict, closed=True):
    evidence: NotRequired["capo_auditmanager.types.evidence.Evidence"]
    """<p> The evidence that the <code>GetEvidence</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceResponse) -> dict:
    out: dict = {}
    if "evidence" in value:
        import capo_auditmanager.types.evidence

        out["evidence"] = capo_auditmanager.types.evidence.serialize_json(
            value["evidence"]
        )
    return out


def deserialize_json(data: dict) -> GetEvidenceResponse:
    out: GetEvidenceResponse = {}  # type: ignore[typeddict-item]
    if "evidence" in data:
        import capo_auditmanager.types.evidence

        out["evidence"] = capo_auditmanager.types.evidence.deserialize_json(
            data["evidence"]
        )
    return out
